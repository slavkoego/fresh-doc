import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


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

    def logout(self):
        log_out = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "span.DD-button__caption")))
        log_out.click()
        log_out2 = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "span.DD-button__caption")))
        log_out2.click()

    def test_login_logout(self):
        driver = self.driver
        self.open_home_page(driver)
        self.find_button_login(driver)
        self.login(driver, username="test.qds.777@bk.ru", password="AnSa1991")
        self.logout()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
