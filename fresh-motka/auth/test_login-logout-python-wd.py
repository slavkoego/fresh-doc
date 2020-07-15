import unittest
import application from Application

class LoginLogout(unittest.TestCase):
    def setUp(self):
        self.app = Application

    def test_login_logout(self):
        driver = self.wd
        self.open_home_page()
        self.find_button_login()
        self.login(username="test.qds.777@bk.ru", password="AnSa1991")
        self.create_new_doc()
        self.logout()

    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()
