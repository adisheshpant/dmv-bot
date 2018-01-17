# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, time
from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.dmv.ca.gov/wasapp/foa/clear.do?goTo=officeVisit&localeName=en"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://www.dmv.ca.gov/wasapp/foa/clear.do?goTo=officeVisit&localeName=en")
        driver.find_element_by_name("officeId").click()
        Select(driver.find_element_by_name("officeId")).select_by_visible_text("SANTA CLARA")
        #Select(driver.find_element_by_name("officeId")).select_by_visible_text("LOS GATOS")
        driver.find_element_by_css_selector("strong").click()
        driver.find_element_by_id("taskCID").click()
        driver.find_element_by_id("first_name").click()
        driver.find_element_by_id("first_name").clear()
        driver.find_element_by_id("first_name").send_keys("STEVE")
        driver.find_element_by_id("last_name").clear()
        driver.find_element_by_id("last_name").send_keys("JOBS")
        driver.find_element_by_id("areaCode").clear()
        driver.find_element_by_id("areaCode").send_keys("669")
        driver.find_element_by_id("telPrefix").clear()
        driver.find_element_by_id("telPrefix").send_keys("232")
        driver.find_element_by_id("telSuffix").clear()
        driver.find_element_by_id("telSuffix").send_keys("8989")
        driver.find_element_by_css_selector("input.btn.btn-primary").click()


        start_date = date(2018, 1, 18) 
        end_date = date(2018, 2, 1)
        for single_date in daterange(start_date, end_date): 
            if single_date.weekday() <= 5: 
                time.sleep(2) 

                el = driver.find_element_by_css_selector("p.no-margin-bottom")
                if el and (not "appointment" in el.text):
                    els = driver.find_elements_by_css_selector("p.no-margin-bottom")
                    for ele in els:
                        print ele.text
                    break

                dtStr = single_date.strftime("%-m_%-d_%Y")
                print "Checking",dtStr
                driver.find_element_by_css_selector("span.ng-button-icon-span").click() 
                element = driver.find_element_by_css_selector("td.ng_cal_date_{}.ng_cal_selectable".format(dtStr)) 
                if element: 
                    element.click() 
                    driver.find_element_by_id("checkAvail").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
   
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
