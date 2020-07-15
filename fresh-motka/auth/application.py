from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.set_window_size(1280, 984)
        self.wd.implicitly_wait(30)

    def open_home_page(self):
            wd = self.wd
            wd.get("http://www.motka-freshdoc.qds.ru/")

    def find_button_login(self):
            wd = self.wd
            wd.find_element_by_css_selector("li.qd__navigation__item > a.js-login.button-login").click()

    def login(self, username, password):
            wd = self.wd
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").send_keys(username)
            wd.find_element_by_name("password").click()
            wd.find_element_by_name("password").send_keys(password)
            wd.find_element_by_css_selector("button.button.expand.qd-overlay-auth__button").click()

    def create_new_doc(self):
            wd = self.wd
            self.wd.find_element(By.LINK_TEXT, "test.qds.777@bk.ru").click()
            self.wd.find_element(By.LINK_TEXT, "Мои шаблоны").click()
            self.wd.find_element_by_css_selector("button > span.DD-button__icon.qd-icon_create-file").click()
            self.wd.find_element(By.LINK_TEXT, "Новый договор").click()
            self.wd.find_element_by_class_name("qd-catalog-dialog-button.qd-catalog-dialog__button.qd-catalog-dialog__button_confirm.qd-catalog-dialog-button__action-target").click()

    def logout(self):
            wd = self.wd
            log_out = WebDriverWait(self.wd, 10).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, "span.DD-button__caption")))
            log_out.click()
    def destroy(self):
        self.wd.quit()
        