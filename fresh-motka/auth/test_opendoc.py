from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestOpendoc():
  def setup_method(self, method):
    self.wd = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.wd.quit()
  
  def test_opendoc(self):
    self.wd.get("http://www.motka-freshdoc.qds.ru/")
    self.wd.set_window_size(1280, 984)

  def find_button_login(self, wd):
    self.wd.find_element_by_css_selector("li.qd__navigation__item > a.js-login.button-login").click()

  def login(self, wd, username, password):
    self.wd.find_element_by_name("email").click()
    self.wd.find_element_by_name("email").send_keys(username)
    self.wd.find_element_by_name("password").click()
    self.wd.find_element_by_name("password").send_keys(password)
    self.wd.find_element_by_css_selector("button.button.expand.qd-overlay-auth__button").click()
    self.wd.find_element(By.LINK_TEXT, "test.qds.777@bk.ru").click()
    self.wd.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[2]/button").click()
    time.sleep(5)
    self.wd.find_element(By.LINK_TEXT, "Типовой договор купли - продажи").click()
time.sleep(5)