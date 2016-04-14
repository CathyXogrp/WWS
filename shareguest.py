# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.webdriver import FirefoxProfile    
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import unittest, time, re, random

class guest(unittest.TestCase):
    ''' share the WWS page to the guest.'''
    def setUp(self):
        LocalProfile ="C:\Users\csun\AppData\Roaming\Mozilla\Firefox\Profiles\zgn6rip8.default"
        profile = FirefoxProfile(LocalProfile)
        self.driver = webdriver.Firefox(profile)
        #self.driver = webdriver.Firefox()
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
        #go to the wedding website
        driver.find_element_by_css_selector("li.nav-item.website > a").click()
        a="".join(random.sample("plmokijnuhbygvctf",5))+"@mailinator.com"
        time.sleep(3)
        #click share
        driver.find_element_by_css_selector("html.js.flexbox.flexboxlegacy.canvas.canvastext.webgl.no-touch.geolocation.postmessage.no-websqldatabase.indexeddb.hashchange.history.draganddrop.websockets.rgba.hsla.multiplebgs.backgroundsize.borderimage.borderradius.boxshadow.textshadow.opacity.cssanimations.csscolumns.cssgradients.no-cssreflections.csstransforms.csstransforms3d.csstransitions.fontface.generatedcontent.video.audio.localstorage.sessionstorage.webworkers.applicationcache.svg.inlinesvg.smil.svgclippaths.breakpoint-desktop body.tk.logged-in div.wrapper div.main-content main div#gs-layout-container.wedding-websites-template.fill-parent div#full-content.gs-container div.gs-left-container.hidden-xs div.left-nav div.actions.clearfix.hidden-xs button#share.btn.btn-primary.pull-right.js-share").click()
        #fill the guest email
        driver.find_element_by_css_selector("html.js.flexbox.flexboxlegacy.canvas.canvastext.webgl.no-touch.geolocation.postmessage.no-websqldatabase.indexeddb.hashchange.history.draganddrop.websockets.rgba.hsla.multiplebgs.backgroundsize.borderimage.borderradius.boxshadow.textshadow.opacity.cssanimations.csscolumns.cssgradients.no-cssreflections.csstransforms.csstransforms3d.csstransitions.fontface.generatedcontent.video.audio.localstorage.sessionstorage.webworkers.applicationcache.svg.inlinesvg.smil.svgclippaths.breakpoint-desktop body.tk.logged-in div.wrapper div.main-content main div#gs-layout-container.wedding-websites-template.fill-parent div#full-content.gs-container div#main-content.gs-content-container div div#message-card div div.form-background div.input-group ul.bubble-input.ui-sortable.bubble-input-current li.bubble.bubble-new.ui-sortable-handle input.edit").clear()
        driver.find_element_by_css_selector("html.js.flexbox.flexboxlegacy.canvas.canvastext.webgl.no-touch.geolocation.postmessage.no-websqldatabase.indexeddb.hashchange.history.draganddrop.websockets.rgba.hsla.multiplebgs.backgroundsize.borderimage.borderradius.boxshadow.textshadow.opacity.cssanimations.csscolumns.cssgradients.no-cssreflections.csstransforms.csstransforms3d.csstransitions.fontface.generatedcontent.video.audio.localstorage.sessionstorage.webworkers.applicationcache.svg.inlinesvg.smil.svgclippaths.breakpoint-desktop body.tk.logged-in div.wrapper div.main-content main div#gs-layout-container.wedding-websites-template.fill-parent div#full-content.gs-container div#main-content.gs-content-container div div#message-card div div.form-background div.input-group ul.bubble-input.ui-sortable.bubble-input-current li.bubble.bubble-new.ui-sortable-handle input.edit").send_keys(a)
        #click send button
        driver.find_element_by_css_selector("html.js.flexbox.flexboxlegacy.canvas.canvastext.webgl.no-touch.geolocation.postmessage.no-websqldatabase.indexeddb.hashchange.history.draganddrop.websockets.rgba.hsla.multiplebgs.backgroundsize.borderimage.borderradius.boxshadow.textshadow.opacity.cssanimations.csscolumns.cssgradients.no-cssreflections.csstransforms.csstransforms3d.csstransitions.fontface.generatedcontent.video.audio.localstorage.sessionstorage.webworkers.applicationcache.svg.inlinesvg.smil.svgclippaths.breakpoint-desktop body.tk.logged-in div.wrapper div.main-content main div#gs-layout-container.wedding-websites-template.fill-parent div#full-content.gs-container div#main-content.gs-content-container div div#message-card div div.form-background div.button-container button#send-message.btn.btn-primary.sm.pull-right").click()
        time.sleep(5)
        #go to the guest's email
        driver.get("http://mailinator.com/")
        time.sleep(10)
        #login the email
        driver.find_element_by_id("inboxfield").clear()
        driver.find_element_by_id("inboxfield").send_keys(a)
        #click go
        driver.find_element_by_xpath("html/body/section[1]/div/div[3]/div[2]/div[2]/div[1]/span/button").click()
        time.sleep(5)
        window_before=driver.window_handles[0]
        driver.find_element_by_css_selector(".innermail.ng-binding").click()
        #driver.find_element_by_xpath(".//*[@id='row_public_1459843351-20004345149-tif']/div[2]/div[2]/div").click()
        time.sleep(5)    
        driver.switch_to_frame(driver.find_element_by_id("publicshowmaildivcontent"))
        #click view
        driver.find_element_by_xpath("html/body/table/tbody/tr[5]/td/a").click()
        #fill PIN
        window_after=driver.window_handles[1]
        driver.switch_to_window(window_after)
        #driver.find_element_by_id("pin").clear()
        #driver.find_element_by_id("pin").send_keys("123")
        #driver.find_element_by_xpath("html/body/div/div/main/div[2]/div/div/div[2]/form/button").click()   
        try:
            WebDriverWait(driver, 10).until(EC.title_contains('gcx'))
        except TimeoutException:
            print 'check point fail 1'
        #driver.find_element_by_id("first-name").clear()
        #driver.find_element_by_id("first-name").send_keys("just")
        #driver.find_element_by_id("last-name").clear()
        #driver.find_element_by_id("last-name").send_keys("for")
        #driver.find_element_by_xpath(".//*[@id='find-invite']").click()
        
        #click RSVP and fill up
        driver.find_element_by_xpath(".//*[@id='content']/div[2]/div[2]/div[5]/div[5]/div/div[4]/button").click()
        driver.find_element_by_xpath(".//*[@id='appendable-rsvp']/div[1]/div/div[2]/input").clear()
        driver.find_element_by_xpath(".//*[@id='appendable-rsvp']/div[1]/div/div[2]/input").send_keys("cath")
        driver.find_element_by_xpath(".//*[@id='appendable-rsvp']/div[1]/div/div[3]/input").clear()
        driver.find_element_by_xpath(".//*[@id='appendable-rsvp']/div[1]/div/div[3]/input").send_keys("sun")
        driver.find_element_by_xpath(".//*[@id='appendable-rsvp']/div[2]/div/div[2]/span[1]/label").click()
        driver.find_element_by_id("rsvp-send").click()
        time.sleep(2)
        driver.find_element_by_id("reminder-email").clear()
        driver.find_element_by_id("reminder-email").send_keys("csun@xogrp.com")
        driver.find_element_by_id("remind-me").click()
        time.sleep(2)
        driver.find_element_by_link_text("PHOTOS").click()
        time.sleep(5) 
        driver.find_element_by_link_text("REGISTRY").click()
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
