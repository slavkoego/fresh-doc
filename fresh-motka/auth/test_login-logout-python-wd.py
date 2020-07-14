import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time


class LoginLogout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1280, 984)
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def open_home_page(self, driver):
        driver.get("http://www.motka-freshdoc.qds.ru/")

    def find_button_login(self, driver):
        driver.find_element_by_css_selector("li.qd__navigation__item > a.js-login.button-login").click()

    def login(self, driver, username, password):
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").send_keys(username)
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_css_selector("button.button.expand.qd-overlay-auth__button").click()

    def create_new_doc (self, driver):
        self.driver.find_element(By.LINK_TEXT, "test.qds.777@bk.ru").click()
        self.driver.find_element(By.LINK_TEXT, "Мои шаблоны").click()
        self.driver.find_element_by_css_selector("button > span.DD-button__icon.qd-icon_create-file").click()
        self.driver.find_element(By.LINK_TEXT, "Новый договор").click()
        self.driver.find_element_by_class_name("qd-catalog-dialog-button.qd-catalog-dialog__button.qd-catalog-dialog__button_confirm.qd-catalog-dialog-button__action-target").click()
        new_doc = self.driver.find_element(By.LINK_TEXT, "Новый договор")
        assert WebDriverWait(self.driver, 3).until(
            ec.alert_is_present(("Вы создали новый документ"))) == new_doc

    def logout(self):
        log_out = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "span.DD-button__caption")))
        log_out.click()


    def test_login_logout(self):
        driver = self.driver
        self.open_home_page(driver)
        self.find_button_login(driver)
        self.login(driver, username="test.qds.777@bk.ru", password="AnSa1991")
        self.create_new_doc(driver)
        self.logout()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
