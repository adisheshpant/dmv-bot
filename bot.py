from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time
from datetime import timedelta, date

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
    driver.find_element_by_id("first_name").send_keys("MICHEAL")
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
        return '\n'.join( [x.text for x in els] )
    return None

def getDriver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    return driver

driver = getDriver()
print(checkLoc(driver, "SANTA CLARA"))
print(checkLoc(driver, "LOS GATOS"))
driver.quit()

"""
# Date range check: check availability for a sequence of dates
# Not required as of now, the dmv site returns the earliest available appointment within next 30 days. 
# Used this if looking for dates after first month.

start_date = date(2018, 1, 18) 
end_date = date(2018, 2, 1)
for single_date in daterange(start_date, end_date): 
    if single_date.weekday() <= 5: 
        time.sleep(2) 

        el = driver.find_element_by_css_selector("p.no-margin-bottom")
        if el and (not "appointment" in el.text):
            els = driver.find_elements_by_css_selector("p.no-margin-bottom")
            for ele in els:
                print(ele.text)
            break

        dtStr = "{dt.month}_{dt.day}_{dt.year}".format(dt=single_date)
        driver.find_element_by_css_selector("span.ng-button-icon-span").click() 
        element = driver.find_element_by_css_selector("td.ng_cal_date_{}.ng_cal_selectable".format(dtStr)) 
        if element: 
            element.click() 
            driver.find_element_by_id("checkAvail").click()
"""
