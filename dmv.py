from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from datetime import timedelta, date, datetime

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def checkLoc(driver, loc):
    driver.get("https://www.dmv.ca.gov/wasapp/foa/clear.do?goTo=officeVisit&localeName=en")
    driver.find_element_by_name("officeId").click()
    Select(driver.find_element_by_name("officeId")).select_by_visible_text(loc)
    driver.find_element_by_css_selector("strong").click()
    driver.find_element_by_id("taskCID").click()
    driver.find_element_by_id("first_name").click()
    driver.find_element_by_id("first_name").clear()
    driver.find_element_by_id("first_name").send_keys("MICHAEL")
    driver.find_element_by_id("last_name").clear()
    driver.find_element_by_id("last_name").send_keys("CORLEONE")
    driver.find_element_by_id("areaCode").clear()
    driver.find_element_by_id("areaCode").send_keys("123")
    driver.find_element_by_id("telPrefix").clear()
    driver.find_element_by_id("telPrefix").send_keys("456")
    driver.find_element_by_id("telSuffix").clear()
    driver.find_element_by_id("telSuffix").send_keys("7890")
    driver.find_element_by_css_selector("input.btn.btn-primary").click()

    el = driver.find_element_by_css_selector("p.no-margin-bottom") 
    if el and (not "appointment" in el.text): 
        els = driver.find_elements_by_css_selector("p.no-margin-bottom") 
        return els[-1].text
    return None

def getDriver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    return driver

dates = {}
loc = ["SANTA CLARA", "LOS GATOS"]

def compare(dateNew, dateOld):
    if dateNew < dateOld:
        retur

def checkDMV(): 
    driver = getDriver() 
    updated = False
    for l in loc: 
        date = checkLoc(driver, l)

        if date:
            date = date.split("at")[0]
            date = datetime.strptime(date, '%A, %B %d, %Y ') 
            if l in dates and dates[l] and date < dates[l]:
                updated = True

        dates[l] = date

    driver.quit()
    return (updated, dates)
