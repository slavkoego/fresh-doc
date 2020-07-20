def test_new_templates(app):
    app.session.open_home_page()
    #app.session.login(username="test.qds.777@bk.ru", password="AnSa1991")
    app.templates.create_new_templates()
    app.templates.rename_new_templates(rename=" переименнованный!")
    app.templates.delete_new_templates()
    app.session.logout()