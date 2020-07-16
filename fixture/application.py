from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.session = SessionHelper(self)
        self.wd.set_window_size(1280, 984)
        self.wd.implicitly_wait(30)

    def create_new_doc(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "test.qds.777@bk.ru").click()
        wd.find_element(By.LINK_TEXT, "Мои шаблоны").click()
        wd.find_element_by_css_selector("button > span.DD-button__icon.qd-icon_create-file").click()
        wd.find_element(By.LINK_TEXT, "Новый договор").click()
        wd.find_element_by_class_name("qd-catalog-dialog-button.qd-catalog-dialog__button.qd-catalog-dialog__button_confirm.qd-catalog-dialog-button__action-target").click()

    def destroy(self):
        self.wd.quit()
