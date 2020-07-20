def test_new_kontragent(app):
    app.session.open_home_page()
    app.session.login(username="test.qds.777@bk.ru", password="AnSa1991")
    app.kontragent.create_new_kontragent()
    app.session.logout()
    