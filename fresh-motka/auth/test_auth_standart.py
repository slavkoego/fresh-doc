from selenium import webdriver
import time
import pytest

link = "http://www.motka-freshdoc.qds.ru"
browser = webdriver.Chrome()
browser.get(link)
input1 = browser.find_element_by_css_selector("div.header--main__wrap .qd__navigation__item .button-login")
input1.click()
time.sleep(2)
login = browser.find_element_by_css_selector(".qd-overlay-auth__input:nth-child(1)")
login.send_keys("test.qds.777@bk.ru")
password = browser.find_element_by_css_selector(".qd-overlay-auth__input:nth-child(2)")
password.send_keys("AnSa1991")
browser.find_element_by_css_selector(".qd-overlay-auth__form .qd-overlay-auth__button").click()
time.sleep(2)
profile = browser.find_element_by_css_selector(" button.DD-button.qd-button_auth.DD-button__action-target > span.DD-button__caption")
profile.click()
time.sleep(2)
logout = browser.find_element_by_css_selector("div.qd-auth-buttons-table.main-controls > button").click()
time.sleep(2)
browser.quit()