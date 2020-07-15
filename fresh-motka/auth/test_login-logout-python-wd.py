import pytest
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_login_logout(app):
    app.open_home_page()
    app.find_button_login()
    app.login(username="test.qds.777@bk.ru", password="AnSa1991")
    app.create_new_doc()
    app.logout()

