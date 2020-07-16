from selenium.webdriver.common.by import By


class PatternHelper():
    def __init__(self, app):
        self.app = app

    def create_new_pattern(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "test.qds.777@bk.ru").click()
        wd.find_element(By.LINK_TEXT, "Мои шаблоны").click()
        wd.find_element_by_css_selector("button > span.DD-button__icon.qd-icon_create-file").click()
        wd.find_element(By.LINK_TEXT, "Новый договор").click()
        wd.find_element_by_class_name("qd-catalog-dialog-button.qd-catalog-dialog__button.qd-catalog-dialog__button_confirm.qd-catalog-dialog-button__action-target").click()

    def delete_new_pattern(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "test.qds.777@bk.ru").click()
        wd.find_element(By.LINK_TEXT, "Мои шаблоны").click()
        wd.find_element(By.CSS_SELECTOR, "div:nth-child(4) > div > button:nth-child(1)").click()
        wd.find_element(By.CLASS_NAME, "qd-filelist-table-item__icon.qd-filelist-table-item__icon_file-template").click()
        wd.find_element(By.CSS_SELECTOR, "div:nth-child(4) > div > button:nth-child(5)").click()
        wd.find_element(By.CSS_SELECTOR, "button.qd-catalog-confirm-button.qd-catalog-confirm__button_confirm.qd-catalog-confirm-button__action-target").click()