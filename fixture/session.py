from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SessionHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://www.motka-freshdoc.qds.ru/")

    def login(self, username, password):
        wd = self.app.wd
        wd.find_element_by_css_selector("li.qd__navigation__item > a.js-login.button-login").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").send_keys(username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_css_selector("button.button.expand.qd-overlay-auth__button").click()

    def logout(self):
        wd = self.app.wd
        log_out = WebDriverWait(self.app.wd, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.DD-button__caption")))
        log_out.click()