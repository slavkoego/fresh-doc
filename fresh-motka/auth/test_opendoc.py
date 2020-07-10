from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestOpendoc():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_opendoc(self):
    self.driver.get("http://www.motka-freshdoc.qds.ru/")
    self.driver.set_window_size(1280, 984)
    self.driver.find_element(By.LINK_TEXT, "test.qds.777@bk.ru").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".qd-filelist-table-item:nth-child(4) .qd-filelist-table-item__field_\\418\\43C\\44F")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.LINK_TEXT, "Мои шаблоны")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".qd-filelist-table-item:nth-child(3) .qd-filelist-table-item__field_\\418\\43C\\44F")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".qd-filelist-table-item:nth-child(2) .qd-filelist-table-item__field_\\418\\43C\\44F").click()
    element = self.driver.find_element(By.LINK_TEXT, "Договоры")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.LINK_TEXT, "Типовой договор купли-продажи").click()
    self.driver.find_element(By.CSS_SELECTOR, ".qd-carcass-btn-save").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".DD-group-flat:nth-child(3) .DD-button:nth-child(2)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".qd-icon_close").click()
    self.driver.find_element(By.CSS_SELECTOR, ".qd-icon_home").click()
  
