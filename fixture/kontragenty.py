from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class KontragentyHelper():
    def __init__(self, app):
        self.app = app

    def create_new_kontragent(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "test.qds.777@bk.ru").click()
        wd.find_element(By.LINK_TEXT, "Контрагенты").click()
        wd.find_element(By.CSS_SELECTOR,
                        "span.DD-button__icon.qd-icon_create-element-location").click()  # create contragent
        weit = WebDriverWait(self.app.wd, 10).until(
            EC.presence_of_element_located((By.ID, "726C65FA-CCB9-4B81-9410-7D5EB2A68421")))
        #weit.click()
        weit.clear()
        weit.send_keys("Иванов Иван Ургантович")
        wd.find_element(By.CSS_SELECTOR, "qd-carcass-btn-save").click()
        wd.find_element(By.CSS_SELECTOR, "qd-icon_close").click()
