# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.firefox.webdriver import FirefoxProfile
import unittest, time, re, random

class wedding(unittest.TestCase):
    ''' create story and wedding info on WWS page.'''
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
        #fill the basic information  
        #click Wedding Website
        driver.find_element_by_css_selector("li.nav-item.website > a").click()
        #choose a theme and click preview
        driver.find_element_by_css_selector("html.js.flexbox.flexboxlegacy.canvas.canvastext.webgl.no-touch.geolocation.postmessage.no-websqldatabase.indexeddb.hashchange.history.draganddrop.websockets.rgba.hsla.multiplebgs.backgroundsize.borderimage.borderradius.boxshadow.textshadow.opacity.cssanimations.csscolumns.cssgradients.no-cssreflections.csstransforms.csstransforms3d.csstransitions.fontface.generatedcontent.video.audio.localstorage.sessionstorage.webworkers.applicationcache.svg.inlinesvg.smil.svgclippaths.breakpoint-desktop.landing body.tk.logged-in.landing div.wrapper div.main-content main div#gs-layout-container.landing-scrollable-container.wedding-websites-template div#landing-container.content-container div.gs-content span#browse-designs-region div div#designs-container.designs-container.row div.col-xs-12 div#designs.row div div.theme-item-container div.theme-item div.masked-overlay div.design-button-container button#preview.btn.white.md.preview").click()
        time.sleep(2)
        #click choose this theme
        driver.find_element_by_css_selector("html.js.flexbox.flexboxlegacy.canvas.canvastext.webgl.no-touch.geolocation.postmessage.no-websqldatabase.indexeddb.hashchange.history.draganddrop.websockets.rgba.hsla.multiplebgs.backgroundsize.borderimage.borderradius.boxshadow.textshadow.opacity.cssanimations.csscolumns.cssgradients.no-cssreflections.csstransforms.csstransforms3d.csstransitions.fontface.generatedcontent.video.audio.localstorage.sessionstorage.webworkers.applicationcache.svg.inlinesvg.smil.svgclippaths.breakpoint-desktop.landing body.tk.logged-in.landing div.wrapper div.main-content main div#gs-layout-container.landing-scrollable-container.wedding-websites-template div#preview-region.gs-preview-region div div.gs-main-nav-region div.gs-main-nav-container.view div.table-cell.hidden-xs div.row div.col-sm-4.gs-choose-theme-container button.btn.btn-primary.use-design").click()
        time.sleep(2)
        e="".join(random.sample("qazwsxedcrfvtgb",3))
        z="".join(random.sample("qazwsxedcrfvtgb",3))
        y="".join(random.sample("qazwsxedcrfvtgb",3))
        x="".join(random.sample("qazwsxedcrfvtgb",3))
        w="".join(random.sample("qazwsxedcrfvtgb",3))
        #fill your first name and last name 
        driver.find_element_by_id("first-name").clear()
        driver.find_element_by_id("first-name").send_keys(z)
        driver.find_element_by_id("last-name").clear()
        driver.find_element_by_id("last-name").send_keys(y)
        #fill your Fiance's first name and last name 
        driver.find_element_by_id("partner-first-name").clear()
        driver.find_element_by_id("partner-first-name").send_keys(x)
        driver.find_element_by_id("partner-last-name").clear()
        driver.find_element_by_id("partner-last-name").send_keys(w)
        driver.find_element_by_id("wedding-date").clear()
        driver.find_element_by_id("wedding-date").send_keys("June 30, 2017")
        driver.find_element_by_id("wedding-location").clear()
        driver.find_element_by_id("wedding-location").send_keys("Seville, Spain")
        #click save and continue
        driver.find_element_by_id("done").click()
        time.sleep(3)
        #click save and continue
        driver.find_element_by_id("done").click()
        #Add story
        #click add your story
        driver.find_element_by_xpath(".//*[@id='right-blocks']/div/div[1]/div[2]/div[1]/p[1]").click()
        #click add a new story
        driver.find_element_by_xpath(".//*[@id='stories_list']/div/div[3]/div/div/div/div/div").click()
        time.sleep(3)
        #add the story title
        driver.find_element_by_id("story-title").clear()
        driver.find_element_by_id("story-title").send_keys(e)
        #add the content of the story
        driver.find_element_by_css_selector("div.redactor-editor.redactor-placeholder").click()
        driver.find_element_by_id("save").click()
        #click Wedding Website
        driver.find_element_by_css_selector("ul.list-horizontal > li > a").click()
        #add wedding info
        #click add wedding info
        driver.find_element_by_xpath("//div[@id='right-blocks']/div/div/div[2]/div[2]/p").click()
        #fill the data
        driver.find_element_by_id("date-field").click()
        driver.find_element_by_xpath("//div[@id='recceremony']/div/div[2]/div/div/button").click()
        #fill the ceremory name
        f="".join(random.sample("qazwsxedcrfvtgb",3))
        driver.find_element_by_name("ceremony-venue-name").clear()
        driver.find_element_by_name("ceremony-venue-name").send_keys(f)
        #fill the reception name
        g="".join(random.sample("qazwsxedcrfvtgb",3))
        driver.find_element_by_name("reception-venue-name").clear()
        driver.find_element_by_name("reception-venue-name").send_keys(g)
        h="".join(random.sample("qazwsxedcrfvtgb",3))
        driver.find_element_by_name("ceremony-full-address").clear()
        driver.find_element_by_name("ceremony-full-address").send_keys(h)
        i="".join(random.sample("qazwsxedcrfvtgb",3))
        driver.find_element_by_name("reception-full-address").clear()
        driver.find_element_by_name("reception-full-address").send_keys(i)
        #click Yes
        driver.find_element_by_css_selector("div.redactor-editor.redactor-placeholder > p").click()
        driver.find_element_by_id("save-wedding").click()
        time.sleep(3)
        #back to Wedding website
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
