import urllib.request
from bs4 import BeautifulSoup
import psycopg
from selenium import webdriver
from selenium.webdriver.support.select import Select
from dataclasses import dataclass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

from catalogue_scraper import Department, syncDepartments, createConnection

@dataclass
class Section:
    crn = ""
    course = ""
    instructor = None
    seats = ""
    start = "" #we'll let SQL handle the tough part
    end = ""
    meetingDays = ""
    meetingTime = ""
    location = ""
    delivery = "" #This should be converted to a lookup table, assuming a certain level of consistency

@dataclass(eq=False)
class Professor:
    first = ""
    last = ""

    def __eq__(self, other):
        if not isinstance(other, Professor):
            return NotImplemented
        return self.first == other.first and self.last == other.last

    def __hash__(self):
        return hash((self.first, self.last))

@dataclass
class Semester:
    short_name = ""
    friendly_name = ""

class SectionScraper:

    def __init__(self):
        self.courses = dict([])
        self.professors = dict([])

    def scrapeSections(self, driver, url):
        #TODO - change records to 100 - not sure if it'll help, but it'll be an accomplishment
        
        driver.get(url)
        try:
            #wait for 2 seconds, or until a table body row with the btnaddcta class is available
            elem = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//tbody/tr/td[contains(@class, 'btnaddcta')]"))) 
        except (Exception) as e:
            #print(e, file=sys.stderr)
            pass

        #Get the number of entries, as a check to make sure we are getting everything
        #Should be in the form 'Showing x to y of n entries
        soup = BeautifulSoup(driver.page_source, "html.parser")
        entries = soup.find("div", {"id": "course_table_info"})
        if entries != None:
            numEntries = int(entries.text.split()[5])


        sections = []
        while True:
            #extract course table
            try:
                soup = BeautifulSoup(driver.page_source, "html.parser")
                courseTableContainer = soup.find("table", {"id": "course_table"})
                courseTable = courseTableContainer.find("tbody")
            except (Exception) as e:
                print(e)
                print("Soup: {0}, Table tage: {1}, Table body: {2}".format(soup == None, courseTableContainer == None, courseTable == None))

            if courseTable == None:
                break
            elif courseTable.find("td", {"class": "dataTables_empty"}) != None:
                break

            sections.extend(self.extractTable(courseTable))

            #find next button
            n = soup.find("li", {"id": "course_table_next"})
            if 'disabled' in n['class']:
                break
            else:
                l = driver.find_element(By.ID, "course_table_next")
                driver.execute_script("arguments[0].click();", l)
                time.sleep(0.1) #a little time for the next page to load

        if len(sections) == 0:
            #print("No sections found in {0}".format(url))
            pass
        elif len(sections) != numEntries: 
            print("Expected {0} sections, found {1}, in {2}".format(numEntries, len(sections), url))
        else:
            #print(numEntries)
            pass

        return sections

    def extractTable(self, courseTable):
        #I'm starting to think this was not designed with scraping in mind...let's try not to get IP banned
        #CRN - btnaddcta
        #Course - crsenumcls
        #Course Title - crse_title
        #Instructor - instructorcls
        #Seats - seats_validation
        #Start and End - datescls
        #Day of Week - dayscls
        #Meeting Times - timescls
        #Location - locationscls
        #Delivery - dlivry_title
        sections = []
        for row in courseTable.find_all("tr"):
            s = Section()
            s.crn = self.findElement(row, "td", "btnaddcta")
            s.course = self.findElement(row, "td", "crsenumcls")

            instructor = self.findElement(row, "td", "instructorcls")
            if instructor != "":
                p = Professor()
                if "," in instructor:
                    p.last = instructor.split(",")[0]
                    p.first = "".join(instructor.split(",")[1:]).strip()
                else:
                    p.last = instructor

                s.instructor = p

            s.seats = self.findElement(row, "td", "seats_validation")
            #start and end
            s.meetingDays = self.findElement(row, "td", "dayscls")
            s.meetingTime = self.findElement(row, "td", "timescls")
            s.location = self.findElement(row, "td", "locationscls")
            s.delivery = self.findElement(row, "td", "dlivry_title")

            #print("{0} {1} {2} {3} {4} {5} {6} {7}".format(s.crn, s.course, s.instructor, s.seats, s.meetingDays, s.meetingTime, s.location, s.delivery))

            sections.append(s)
            
        return sections

    def syncSections(self, sections, semester, conn):
        selectSQL = "SELECT id FROM catalogue_section WHERE semester = %s AND course_id = %s AND professor_id = %s AND delivery_type = %s AND offering_days = %s AND offering_time = %s;"
        updateSQL = """UPDATE catalogue_section 
                    SET offering_time = %s,
                        professor_id = users_professor.id,
                        delivery_type = %s,
                        course_id = catalogue_course.id
                    FROM users_professor, catalogue_course
                    WHERE catalogue_section.id = %s
                        AND users_professor.first_name = %s AND users_professor.last_name = %s
                        AND catalogue_course.department || ' ' || catalogue_course.number = %s;"""
        insertSQL = """INSERT INTO catalogue_section ( semester, course_id, professor_id, delivery_type, offering_days, offering_time )
                    VALUES (%s, %s, %s, %s, %s, %s );"""

        cur = conn.cursor()

        #loop through all the sections
        for s in sections:
            #check for professor
            #print("{0}|{1}|{2}|{3}".format(s.instructor.first, s.instructor.last, s.instructor in professors, s.instructor != None))
            if not s.instructor in self.professors and s.instructor != None:
                self.addProfessor(s.instructor, conn)
            
            if s.instructor == None:
                profID = 0
            else:
                profID = self.professors[s.instructor]

            if not s.course in self.courses and s.course != None:
                self.addCourse(s.course, conn)

            if s.course == None:
                courseID = 0
            else:
                courseID = self.courses[s.course]

            try:
                #add or update the section
                cur.execute(selectSQL, (semester, courseID, profID, s.delivery, s.meetingDays, s.meetingTime ))
                if cur.rowcount == 0:
                    cur.execute(insertSQL, ((semester, courseID, profID, s.delivery, s.meetingDays, s.meetingTime )))

                if cur.rowcount != 1:
                    print("Error with section {0}, please review to make sure {1} {2} or {3} are in the database".format(s.crn, s.instructor.first, s.instructor.last, s.course))
            except (Exception) as e:
                print(e)
            conn.commit()
            
        cur.close()

    def addProfessor(self, name, conn):
        selectSQL = "SELECT id FROM users_professor WHERE first_name = %s AND last_name = %s;"
        insertSQL = "INSERT INTO users_professor ( first_name, last_name, email, is_professor ) VALUES (%s, %s, '', TRUE) RETURNING id;"

        cur = conn.cursor()

        cur.execute(selectSQL, (name.first, name.last))
        if cur.rowcount == 0:
            cur.execute(insertSQL, (name.first, name.last))

        self.professors[name] = cur.fetchone()[0]

        conn.commit()
        cur.close()

    def addCourse(self, course, conn):
        selectSQL = "SELECT id FROM catalogue_course WHERE department = %s AND number = %s;"
        insertSQL = "INSERT INTO catalogue_course ( department, number, name, description, credits ) VALUES (%s, %s, '', '', '') RETURNING id;"
        d = course.split()[0]
        n = course.split()[1]

        cur = conn.cursor()

        cur.execute(selectSQL, (d, n))
        if cur.rowcount == 0:
            cur.execute(insertSQL, (d, n))

        self.courses[course] = cur.fetchone()[0]


    def findElement(self, o, tag, cls):
        if o.find(tag, class_=cls) != None: 
            return o.find(tag, class_=cls).text
        else:
            return ""

    def scrapeTerms(self, driver):
        url = "https://courses.odu.edu/"
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")

        results = soup.find(id="course-search-term")
        
        #Load terms from the main page first
        terms = []
        for element in results.find_all("option"):
            if element['value'] != "": 
                t = Semester()
                t.short_name = element['value']
                t.friendly_name = element.text
                if '(' in t.friendly_name:
                    t.friendly_name = t.friendly_name[:t.friendly_name.index('(')]

                terms.append(t)

        return terms

    def syncTerms(self, terms, conn):
        selectSQL = "SELECT ID FROM catalogue_semester WHERE short_name = %s;"
        #read only should be true for new semesters
        #long term, there should be an automatic process to update readonly 
        insertSQL = "INSERT INTO catalogue_semester ( short_name, friendly_name, readonly ) VALUES (%s, %s, TRUE);"

        cur = conn.cursor()

        for t in terms:
            cur.execute(selectSQL, (t.short_name, ))

            if cur.rowcount == 0:
                cur.execute(insertSQL, (t.short_name, t.friendly_name))

        conn.commit()
        cur.close()

    def scrapeDepartments(self, driver, term):
        #if we just search for the term, it will give us a list of departments in that term
        #OK, thats a lie, but there is some level of filtering
        url = "https://courses.odu.edu/search?subject=&term={0}&".format(term)

        driver.get(url)
        elem = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "subjectmain"))) 

        soup = BeautifulSoup(driver.page_source, "html.parser")
        departmentElements = soup.find_all("input", {"name": "subjectmain"})

        departments = []
        for element in departmentElements:
            d = Department()

            label = soup.find("label", {"for": element['id']})
            if label != None:            
                d.abbreviation = element['value']
                d.name = label.text.split(":")[0].strip()

                departments.append(d)
            else:
                print("Could not find {0}".format(element['id']))

        return departments


if __name__ == "__main__":
    #This is a little harder than the course catalog
    #portions are loaded by JavaScript (may it suffer a thousand indignities), so we actually have to simulate a webpage
    options  = webdriver.FirefoxOptions()
    options.add_argument("--headless")

    scraper = SectionScraper()

    driver = webdriver.Firefox(options=options)
    
    terms = scraper.scrapeTerms(driver)

    conn = ""
    conn = createConnection()

    if conn != None:
        scraper.syncTerms(terms, conn)
        #search url is in the form https://courses.odu.edu/search?subject=<>&term=<>&
        for t in terms:
            departments = scraper.scrapeDepartments(driver, t.short_name)
            syncDepartments(departments, conn)

            for d in departments:
                url = "https://courses.odu.edu/search?subject={0}&term={1}&".format(d.abbreviation, t.short_name)
                
                try:
                    s = scraper.scrapeSections(driver, url)
                    if s != None: scraper.syncSections(s, t.short_name, conn)
                except (Exception) as error:
                    print(error)
                    print(url)

    driver.close()
    driver.quit()