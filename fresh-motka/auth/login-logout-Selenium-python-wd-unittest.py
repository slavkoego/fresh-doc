import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait



class LoginLogout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login_logout(self):
        driver = self.driver
        # Label: Open home page
        driver.get("http://www.motka-freshdoc.qds.ru/")
        # Label: Click buttons "Войти"
        driver.find_element_by_css_selector("li.qd__navigation__item > a.js-login.button-login").click()
        # Label: Test login
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").send_keys("test.qds.777@bk.ru")
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").send_keys("AnSa1991")
        driver.find_element_by_css_selector("button.button.expand.qd-overlay-auth__button").click()
        # Label: Test Logout
        login_out = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "span.DD-button__caption")))
        login_out.click()
        login_out2 = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "span.DD-button__caption")))
        login_out2.click()


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
