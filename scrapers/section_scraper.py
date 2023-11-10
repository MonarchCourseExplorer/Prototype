import urllib.request
from bs4 import BeautifulSoup
import psycopg2
from selenium import webdriver

if __name__ == "__main__":
    url = "https://courses.odu.edu/"

    #This is a little harder than the course catalog
    #portions are loaded by JavaScript (may it suffer a thousand indignities), so we actually have to simulate a webpage
    options  = webdriver.FirefoxOptions()
    options.add_argument("--headless")

    driver = webdriver.Firefox(options=options)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    results = soup.find(id="course-search-term")
    
    #Load terms and departments from the main page first
    terms = []
    for element in results.find_all("option"):
        terms.append(element['value'])

    departments = [] #This could probably be pulled from the DB, but this should ensure we don't get an invalid department
    results = soup.find(id="sub-dropdown-list")
    
    for element in results.find_all("li"):
        departments.append(element.find("input")['value'])

    driver.close