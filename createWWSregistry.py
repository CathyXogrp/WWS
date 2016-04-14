# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.firefox.webdriver import FirefoxProfile
import unittest, time, re, random

class Registry(unittest.TestCase):
    ''' create registry on WWS page.'''
    def setUp(self):
        LocalProfile ="C:\Users\csun\AppData\Roaming\Mozilla\Firefox\Profiles\zgn6rip8.default"
        profile = FirefoxProfile(LocalProfile)
        self.driver = webdriver.Firefox(profile)
        #self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://qa-beta.theknot.com/dashboard"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_create(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath("//ul[@id='mobile-nav']/div/div/li[8]/button").click()
        time.sleep(8)
        signup_frame = driver.find_element_by_css_selector("#modal > iframe")
        driver.switch_to_frame(signup_frame)
        driver.find_element_by_xpath("/html/body/div/div/main/div/section/div/form/p[2]/small/span[2]/a").click()
        time.sleep(2)
        #login
        driver.find_element_by_id("wizard_email").clear()
        driver.find_element_by_id("wizard_email").send_keys("ken@mailinator.com")
        driver.find_element_by_id("wizard_password").clear()
        driver.find_element_by_id("wizard_password").send_keys("aaaaaa")
        driver.find_element_by_name("button").click()
        time.sleep(8)   
        #go to wedding website
        driver.find_element_by_css_selector("li.nav-item.website > a").click()
        driver.find_element_by_css_selector("ul.list-horizontal > li > a").click()
        time.sleep(2) 
        #click add registry  
        driver.find_element_by_xpath(".//*[@id='registry-region']/div/p[1]").click()
        time.sleep(2)
        #click create registry
        driver.find_element_by_id("create-registry").click()
        window_before=driver.window_handles[0]
        #choose one registry
        driver.find_element_by_xpath(".//*[@id='retailer']/div[14]/a/div").click()
        window_after=driver.window_handles[1]
        driver.switch_to_window(window_after)
        time.sleep(5)
        #sign in on registry page
        driver.find_element_by_link_text("Create a Registry").click()
        driver.find_element_by_link_text("Create one").click()
        a="".join(random.sample("qazwsxedcrfvtgbplikojuh",4))
        driver.find_element_by_id("fld-firstName").clear()
        driver.find_element_by_id("fld-firstName").send_keys(a)
        b="".join(random.sample("qazwsxedcrfvtgbplikojuh",4))
        driver.find_element_by_id("fld-lastName").clear()
        driver.find_element_by_id("fld-lastName").send_keys(b)
        z="".join(random.sample("qazwsxedcrfvtgbplikojuh",4))+"@xogrp.com"
        driver.find_element_by_id("fld-e").clear()
        driver.find_element_by_id("fld-e").send_keys(z)
        driver.find_element_by_id("fld-p1").clear()
        driver.find_element_by_id("fld-p1").send_keys("1q2w3e4r5")
        driver.find_element_by_id("fld-p2").clear()
        driver.find_element_by_id("fld-p2").send_keys("1q2w3e4r5")
        c="".join(random.sample("0236985741",10))
        driver.find_element_by_id("fld-phone").clear()
        driver.find_element_by_id("fld-phone").send_keys("8756894254")
        time.sleep(3)
        #create registry to the next page.
        driver.find_element_by_xpath("html/body/section/div/div[1]/div[1]/div/form/button").click()
        #add married info
        d="".join(random.sample("qazwsxedcrfvtgbplikojuh",4))
        driver.find_element_by_name("list-notes.first-name").clear()
        driver.find_element_by_name("list-notes.first-name").send_keys(d)
        e="".join(random.sample("qazwsxedcrfvtgbplikojuh",4))
        driver.find_element_by_name("list-notes.last-name").clear()
        driver.find_element_by_name("list-notes.last-name").send_keys(e)
        f="".join(random.sample("qazwsxedcrfvtgbplikojuh",4))
        driver.find_element_by_name("co-registrant-first-name").clear()
        driver.find_element_by_name("co-registrant-first-name").send_keys(f)
        g="".join(random.sample("qazwsxedcrfvtgbplikojuh",4))
        driver.find_element_by_name("co-registrant-last-name").clear()
        driver.find_element_by_name("co-registrant-last-name").send_keys(g)
        driver.find_element_by_name("occasion-date").clear()
        driver.find_element_by_name("occasion-date").send_keys("09/30/2016")
        time.sleep(3)
        driver.find_element_by_xpath(".//*[@id='js-seed-steps']/div/div/div/div/p/button").click()
        #step 3.where should guests send your gifts?
        h="".join(random.sample("qazwsxedcrfvtgbplikojuh",4))
        driver.find_element_by_name("first-name").clear()
        driver.find_element_by_name("first-name").send_keys(h)
        i="".join(random.sample("qazwsxedcrfvtgbplikojuh",4))
        driver.find_element_by_name("last-name").clear()
        driver.find_element_by_name("last-name").send_keys(i)
        driver.find_element_by_name("address-line1").clear()
        driver.find_element_by_name("address-line1").send_keys("Xogrp company")
        driver.find_element_by_name("address-city").clear()
        driver.find_element_by_name("address-city").send_keys("NewYork")
        driver.find_element_by_name("address-zip").clear()
        driver.find_element_by_name("address-zip").send_keys("94203")
        mySelect=Select(driver.find_element_by_name("address-state"))
        mySelect.select_by_visible_text("AK - Alaska")
        driver.find_element_by_name("phone-number").clear()
        driver.find_element_by_name("phone-number").send_keys("8756894254")
        time.sleep(3)
        #click keep the address
        driver.find_element_by_xpath(".//*[@id='js-seed-steps']/div/div/div/div/div/p[1]/button").click()
        time.sleep(3)
        driver.find_element_by_css_selector("html body.has-animations.has-localstorage.has-respond.has-svg.has-transform2D.no-local.no-mobile.no-touch.size-l.modal-open div div.modal.fade.sample-modal.in div.modal-dialog.modal-lg div.modal-content div.modal-body div.standardize-error__body button.btn.btn-lg.btn-primary.js-keep.standardize-error__button").click()
        time.sleep(3)
        driver.find_element_by_xpath(".//*[@id='js-seed-steps']/div/div/div/div/p[1]/button").click()
        time.sleep(3)


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
