# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.firefox.webdriver import FirefoxProfile
import unittest, time, re, random

class events(unittest.TestCase):
    ''' create event on WWS page.'''
    def setUp(self):
        LocalProfile ="C:\Users\csun\AppData\Roaming\Mozilla\Firefox\Profiles\zgn6rip8.default"
        profile = FirefoxProfile(LocalProfile)
        self.driver = webdriver.Firefox(profile)
        self.driver.implicitly_wait(30)
        self.base_url = "https://qa-beta.theknot.com/dashboard"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_story_wedding_event(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath("//ul[@id='mobile-nav']/div/div/li[8]/button").click()
        time.sleep(8)
        signup_frame = driver.find_element_by_css_selector("#modal > iframe")
        driver.switch_to_frame(signup_frame)
        driver.find_element_by_xpath("/html/body/div/div/main/div/section/div/form/p[2]/small/span[2]/a").click()
        time.sleep(2)
        #Login
        driver.find_element_by_id("wizard_email").clear()
        driver.find_element_by_id("wizard_email").send_keys("ken@mailinator.com")
        driver.find_element_by_id("wizard_password").clear()
        driver.find_element_by_id("wizard_password").send_keys("aaaaaa")
        driver.find_element_by_name("button").click()
        #go to wedding website
        driver.find_element_by_css_selector("li.nav-item.website > a").click()
        driver.find_element_by_css_selector("ul.list-horizontal > li > a").click()
        #add event
        driver.find_element_by_xpath("//div[@id='right-blocks']/div/div/div[2]/div[3]/p").click()
        driver.find_element_by_css_selector("div.gallery-add-title").click()
        #fill the date
        driver.find_element_by_id("date-input").click()
        driver.find_element_by_link_text("31").click()
        j="".join(random.sample("qazwsxedcrfvtgb",3))
        driver.find_element_by_name("event-venue-name").clear()
        driver.find_element_by_name("event-venue-name").send_keys(j)
        driver.find_element_by_name("event-full-address").clear()
        driver.find_element_by_name("event-full-address").send_keys("Seville, Spain")
        #click Yes
        driver.find_element_by_css_selector("div.redactor-editor.redactor-placeholder").click()
        driver.find_element_by_xpath("//div[@id='dialog-container']/div/div/div/div/div[3]/button").click()
        k="".join(random.sample("qazwsxedcrfvtgb",3))
        driver.find_element_by_id("name-input").clear()
        driver.find_element_by_id("name-input").send_keys(k)
        #click save
        driver.find_element_by_xpath("//div[@id='dialog-container']/div/div/div/div/div[3]/button").click()
        #back to wedding website
        driver.find_element_by_css_selector("ul.list-horizontal > li > a").click()
        time.sleep(10)
        

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
