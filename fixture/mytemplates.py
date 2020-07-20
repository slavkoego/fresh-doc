from selenium.webdriver.common.by import By


class MytemplatesHelper():
    def __init__(self, app):
        self.app = app

    def create_new_templates(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "test.qds.777@bk.ru").click()
        wd.find_element(By.LINK_TEXT, "Мои шаблоны").click()
        wd.find_element_by_css_selector("button > span.DD-button__icon.qd-icon_create-file").click()   #кнопка добавить
        wd.find_element(By.LINK_TEXT, "Новый договор").click()
        wd.find_element_by_class_name("qd-catalog-dialog-button.qd-catalog-dialog__button.qd-catalog-dialog__button_confirm.qd-catalog-dialog-button__action-target").click()

    def rename_new_templates(self, rename):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "div:nth-child(4) > div > button:nth-child(1)").click()
        wd.find_element(By.CSS_SELECTOR, "span.qd-filelist-table-item__field.qd-filelist-table-item__field_Наименование.DD-style-3f").send_keys(
            rename)
        wd.find_element(By.CSS_SELECTOR, "div:nth-child(4) > div > button:nth-child(1)").click()


    def delete_new_templates(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "test.qds.777@bk.ru").click()
        wd.find_element(By.LINK_TEXT, "Мои шаблоны").click()
        wd.find_element(By.CSS_SELECTOR, "div:nth-child(4) > div > button:nth-child(1)").click()                            #кнопка режим правки
        wd.find_element(By.CLASS_NAME, "qd-filelist-table-item__icon.qd-filelist-table-item__icon_file-template").click()   #выбираем шаблон
        wd.find_element(By.CSS_SELECTOR, "div:nth-child(4) > div > button:nth-child(5)").click()                            #кнопка удалить
        wd.find_element(By.CSS_SELECTOR, "button.qd-catalog-confirm-button.qd-catalog-confirm__button_confirm.qd-catalog-confirm-button__action-target").click() #подтвердить удаление
