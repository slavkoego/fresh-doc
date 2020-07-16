from selenium import webdriver
from fixture.session import SessionHelper
from  fixture.doc import DocHelper



class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.session = SessionHelper(self)
        self.doc = DocHelper(self)
        self.wd.set_window_size(1280, 984)
        self.wd.implicitly_wait(30)

    def destroy(self):
        self.wd.quit()
