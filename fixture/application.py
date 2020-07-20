from selenium import webdriver
from fixture.session import SessionHelper
from fixture.mytemplates import MytemplatesHelper
from fixture.kontragenty import KontragentyHelper



class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.session = SessionHelper(self)
        self.templates = MytemplatesHelper(self)
        self.kontragent = KontragentyHelper(self)
        self.wd.set_window_size(1280, 984)
        self.wd.implicitly_wait(30)

    def destroy(self):
        self.wd.quit()
