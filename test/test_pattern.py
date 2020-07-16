

def test_new_pattern(app):
    app.session.open_home_page()
    #app.session.login(username="test.qds.777@bk.ru", password="AnSa1991")
    app.pattern.create_new_pattern()
    app.pattern.delete_new_pattern()
    app.session.logout()