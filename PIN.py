# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.firefox.webdriver import FirefoxProfile
import unittest, time, re


class PIN(unittest.TestCase):
    ''' create PIN on WWS page.'''
    def setUp(self):
        LocalProfile ="C:\Users\csun\AppData\Roaming\Mozilla\Firefox\Profiles\zgn6rip8.default"
        profile = FirefoxProfile(LocalProfile)
        self.driver = webdriver.Firefox(profile)
        self.driver.implicitly_wait(30)
        self.base_url = "https://qa-beta.theknot.com/dashboard"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_p_i_n(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath("//ul[@id='mobile-nav']/div/div/li[8]/button").click()
        time.sleep(8)
        signup_frame = driver.find_element_by_css_selector("#modal > iframe")
        driver.switch_to_frame(signup_frame)
        #login
        driver.find_element_by_xpath("/html/body/div/div/main/div/section/div/form/p[2]/small/span[2]/a").click()
        time.sleep(2)
        driver.find_element_by_id("wizard_email").clear()
        driver.find_element_by_id("wizard_email").send_keys("ken@mailinator.com")
        driver.find_element_by_id("wizard_password").clear()
        driver.find_element_by_id("wizard_password").send_keys("aaaaaa")
        driver.find_element_by_name("button").click()
        time.sleep(5)
        #go to wedding website
        driver.find_element_by_css_selector("html.js.flexbox.flexboxlegacy.canvas.canvastext.webgl.no-touch.geolocation.postmessage.no-websqldatabase.indexeddb.hashchange.history.draganddrop.websockets.rgba.hsla.multiplebgs.backgroundsize.borderimage.borderradius.boxshadow.textshadow.opacity.cssanimations.csscolumns.cssgradients.no-cssreflections.csstransforms.csstransforms3d.csstransitions.fontface.generatedcontent.video.audio.localstorage.sessionstorage.webworkers.applicationcache.svg.inlinesvg.smil.svgclippaths.breakpoint-desktop body.tk.logged-in div.wrapper div.main-content main div.content-container section#mainRegion.main.container div#plannerMain.planner-main div.dashboard-container.row div.sidebar-container.col-sm-3 div#sidebar.sidebar div#sidebar-menu div div#accordion.panel-group div.panel div#nav-sidebar.panel-collapse.collapse ul.nav-sidebar li.nav-item.website a").click()
        time.sleep(2)
        #click settings
        driver.find_element_by_id("settings-nav").click()
        time.sleep(5)
        #click on Yes
        driver.find_element_by_xpath(".//*[@id='dialog-container']/div/div/div/div/div[2]/div[3]/div[1]/div/label/div[2]").click()
        driver.find_element_by_xpath(".//*[@id='dialog-container']/div/div/div/div/div[2]/div[3]/div[2]/div[1]/label/div[2]").click()
        #fill the PIN
        driver.find_element_by_xpath(".//*[@id='dialog-container']/div/div/div/div/div[2]/div[3]/div[2]/div[2]/input").clear()
        driver.find_element_by_xpath(".//*[@id='dialog-container']/div/div/div/div/div[2]/div[3]/div[2]/div[2]/input").send_keys("123")
        driver.find_element_by_id("save-settings").click()
        time.sleep(5)
    
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
