import requests
from bs4 import BeautifulSoup
from course import Course
import psycopg

def scrapeDepartments():
    page = requests.get("https://catalog.odu.edu/courses/")

    soup = BeautifulSoup(page.content, "html.parser")

    departmentUrls = []

    results = soup.find("div", class_="sitemap")

    department_elements = soup.find_all("a", class_="sitemaplink", href=True)

    for element in department_elements:
        departmentUrls.append("https://catalog.odu.edu" + element["href"])

    return departmentUrls

def scrapeCourses(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    courses = []
    courseBlocks = ["undergraduatecoursestextcontainer", "graduatecoursestextcontainer"]

    for block in courseBlocks:
        results = soup.find(id=block)

        course_elements = results.find_all("div", class_="courseblock") #these are the individual courses blocks

        for element in course_elements:
            number = element.find("span", class_="detail-xrefcode").text

            titleElement = element.find("span", class_="detail-title")
            if titleElement != None: title = titleElement.text

            hours = element.find("span", class_="detail-hours_html").text

            detailElement = element.find("p", class_="courseblockextra")
            if detailElement != None: detail = detailElement.text #apparently this is allowed to be blank
            
            prereqs = element.find("span", class_="detail-prereq")

            c = Course.parseCourse(number, title, hours, detail)
            courses.extend(c)

    return courses

def syncCourses(courses):
    conn = createConnection()
    selectSQL = "SELECT ID FROM catalogue_course WHERE department = %s AND number = %s;"
    insertSQL = """INSERT INTO catalogue_course ( department, number, name, credits, description ) 
          VALUES (%s, %s, %s, %s, %s);"""
    updateSQL = """UPDATE catalogue_course 
            SET name = %s, credits = %s, description = %s
            WHERE ID = %s;"""

    if conn != None:
        cur = conn.cursor()

        for course in courses:
            #check and see if the course is already in the table - match department and number
            cur.execute(selectSQL, (course.department, course.number))

            if cur.rowcount > 0:
                #if yes, update it - shouldn't we check to see if any updates are necessary? Logically yes, but how bad is the performance from NOT checking?
                cur.execute(updateSQL, (course.title, course.credits, course.detail, cur.fetchone()[0]))
            else:
                #if not, insert it
                cur.execute(insertSQL, (course.department, course.number, course.title, course.credits, course.detail))

        conn.commit()
        cur.close()
        conn.close()


def createConnection():
    conn = None

    try:
        #This is SUPER bad practice, but...it's already out there
        conn = psycopg.connect(host="postgres",
            dbname="mce_django",
            user="qrAKoIzpncvkHaCzUeBwGkXnhKgVypHZ",
            password="yVzY2BMfTNn4jW4pPr3Xcvuz0St5snmVPPJiHEFc1oP4O3JMlJcYOjzkZSxzAgJO")
    except (Exception) as error:
        print(error)

    return conn

if __name__ == "__main__":
    urls = scrapeDepartments()

    for url in urls:
        courses = scrapeCourses(url)
        syncCourses(courses)