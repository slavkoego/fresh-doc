from selenium import webdriver
from fixture.session import SessionHelper
from fixture.my_pattern import PatternHelper



class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.session = SessionHelper(self)
        self.pattern = PatternHelper(self)
        self.wd.set_window_size(1280, 984)
        self.wd.implicitly_wait(30)

    def destroy(self):
        self.wd.quit()
