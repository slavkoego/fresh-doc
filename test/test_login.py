
def test_login_logout(app):
    app.session.open_home_page()
    app.session.login(username="test.qds.777@bk.ru", password="AnSa1991")
    app.session.logout()




