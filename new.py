# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.firefox.webdriver import FirefoxProfile
import unittest, time, re

class Ex17(unittest.TestCase):
    ''' create a new account'''
    def setUp(self):
        LocalProfile ="C:\Users\csun\AppData\Roaming\Mozilla\Firefox\Profiles\zgn6rip8.default"
        profile = FirefoxProfile(LocalProfile)
        self.driver = webdriver.Firefox(profile)
        self.driver.implicitly_wait(30)
        self.base_url = "https://qa-beta.theknot.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ex17(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath("//ul[@id='mobile-nav']/div/div/li[8]/button").click()
        time.sleep(8)
        signup_frame = driver.find_element_by_css_selector("#modal > iframe")
        driver.switch_to_frame(signup_frame)
        #z="".join(random.sample("qazwsxedcrfvtgbplmoknijb",4))+"@mailinator.com"
        driver.find_element_by_id("wizard_email").clear()
        driver.find_element_by_id("wizard_email").send_keys("ken@mailinator.com")
        driver.find_element_by_id("wizard_password").clear()
        driver.find_element_by_id("wizard_password").send_keys("aaaaaa")
        driver.find_element_by_name("button").click()
        time.sleep(8)
        driver.find_element_by_xpath("/html/body/div/div/main/div/section/div/form/div[3]/button").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/div/main/div/section/div/form/div[3]/ul/li[1]/span").click()
        time.sleep(2)
        driver.find_element_by_name("button").click()
        driver.find_element_by_css_selector("html.js.flexbox.flexboxlegacy.canvas.canvastext.webgl.no-touch.geolocation.postmessage.no-websqldatabase.indexeddb.hashchange.history.draganddrop.websockets.rgba.hsla.multiplebgs.backgroundsize.borderimage.borderradius.boxshadow.textshadow.opacity.cssanimations.csscolumns.cssgradients.no-cssreflections.csstransforms.csstransforms3d.csstransitions.fontface.no-generatedcontent.video.audio.localstorage.sessionstorage.webworkers.applicationcache.svg.inlinesvg.smil.svgclippaths.breakpoint-mobile.breakpoint-desktop body.tk.proactive.role.engagement_date_step div.wrapper div.main-content main div#wizard section.matriculation.module.container div.main form#new_wizard.new_wizard a#global-exit-button.exit.icon-container.icon-holster span.icon.icon-general-close").click()
        driver.find_element_by_id("sign_up").click()
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
