from selenium import webdriver

link = "http://www.motka-freshdoc.qds.ru"
browser = webdriver.Chrome()
browser.get(link)
input1 = browser.find_element_by_css_selector("div.header--main__wrap .qd__navigation__item .button-login")
input1.click()

login = browser.find_element_by_css_selector(".qd-overlay-auth__input:nth-child(1)")
login.send_keys("test.qds.777@bk.ru")
password = browser.find_element_by_css_selector(".qd-overlay-auth__input:nth-child(2)")
password.send_keys("AnSa1991")
browser.find_element_by_css_selector(".qd-overlay-auth__form .qd-overlay-auth__button").click()


browser.quit()