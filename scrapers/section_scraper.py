import urllib.request
from bs4 import BeautifulSoup
import psycopg2
from selenium import webdriver
from selenium.webdriver.support.select import Select
from dataclasses import dataclass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@dataclass
class Section:
    crn = ""
    course = ""
    instructor = ""
    seats = ""
    start = "" #we'll let SQL handle the tough part
    end = ""
    meetingDays = ""
    meetingTime = ""
    location = ""
    delivery = "" #This should be converted to a lookup table, assuming a certain level of consistency

def scrapeSections(driver, url):
    #TODO - change records to 100 - not sure if it'll help, but it'll be an accomplishment
    
    driver.get(url)

    try:
        #wait for 5 seconds, or until an even row is available - yes, this doesn't work if there is only 1 section, but it is good enough
        elem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "even"))) 
    except (Exception) as e:
        print(e)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    courseTable = soup.find("table", {"id": "course_table"})
    courseTable = courseTable.find("tbody")
    

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
    for row in courseTable.find_all("tr"):
        s = Section()
        s.crn = findElement(row, "td", "btnaddcta")
        s.course = findElement(row, "td", "crsenumcls")
        s.instructor = findElement(row, "td", "instructorcls")
        s.seats = findElement(row, "td", "seats_validation")
        #start and end
        s.meetingDays = findElement(row, "td", "dayscls")
        s.meetingTime = findElement(row, "td", "timescls")
        s.location = findElement(row, "td", "locationscls")
        s.delivery = findElement(row, "td", "dlivry_title")
        
        print("{0} {1} {2} {3} {4} {5} {6} {7}".format(s.crn, s.course, s.instructor, s.seats, s.meetingDays, s.meetingTime, s.location, s.delivery))

def findElement(o, tag, cls):
    if o.find(tag, class_=cls) != None: 
        return o.find(tag, class_=cls).text
    else:
        return ""

if __name__ == "__main__":
    url = "https://courses.odu.edu/"

    #This is a little harder than the course catalog
    #portions are loaded by JavaScript (may it suffer a thousand indignities), so we actually have to simulate a webpage
    options  = webdriver.FirefoxOptions()
    #options.add_argument("--headless")

    driver = webdriver.Firefox(options=options)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    results = soup.find(id="course-search-term")
    
    #Load terms and departments from the main page first
    terms = []
    for element in results.find_all("option"):
        if element['value'] != "": terms.append(element['value'])

    departments = [] #This could probably be pulled from the DB, but this should ensure we don't get an invalid department
    results = soup.find(id="sub-dropdown-list")
    
    for element in results.find_all("li"):
        departments.append(element.find("input")['value'])

    #search url is in the form https://courses.odu.edu/search?subject=<>&term=<>&
    for t in terms:
        for d in departments:
            url = "https://courses.odu.edu/search?subject={0}&term={1}&".format(d, t)
            
            print(url)
            try:
                scrapeSections(driver, url)
            except (Exception) as error:
                print(error)
            break
        break

    url = "https://courses.odu.edu/search?subject=CS&term=202410&"
    scrapeSections(driver, url)

    #driver.close()
    #driver.quit()