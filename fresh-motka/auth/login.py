from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://www.motka-freshdoc.qds.ru/")
        driver.find_element_by_css_selector("li.qd__navigation__item > a.js-login.button-login").click()
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("test.qds.777@bk.ru")
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("AnSa1991")
        driver.find_element_by_css_selector("button.button.expand.qd-overlay-auth__button").click()
        driver.find_element_by_xpath("//div[@id='catalog_63782293']/div/div/div/div[3]/a/span[3]").click()
        driver.find_element_by_css_selector("span.DD-button__icon.qd-icon_create-file").click()
        driver.find_element_by_xpath("//div[@id='catalog_63782293']/div/div[2]/div/div[6]/a/span[3]").click()
        driver.find_element_by_css_selector("div.qd-catalog-dialog-button.qd-catalog-dialog__button.qd-catalog-dialog__button_confirm.qd-catalog-dialog-button__action-target").click()
        driver.find_element_by_xpath("//div[@id='catalog_63782293']/div/div/div/div[4]/a/span[3]").click()
        driver.find_element_by_id("E321B633-A0D4-4346-9F9F-79686BE31F62").click()
        # ERROR: Caught exception [unknown command [editContent]]
        driver.find_element_by_css_selector("span.DD-button__icon.qd-carcass-btn-save").click()
        driver.find_element_by_css_selector("span.qd-control-menuitem-caption").click()
        driver.find_element_by_css_selector("span.DD-button__icon.qd-icon_close").click()
        driver.find_element_by_css_selector("span.DD-button__caption").click()
        driver.find_element_by_css_selector("button.qd-global-button.qd-glb-btn-reset").click()
    
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
