import pytest

from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_login_logout(app):
    app.session.open_home_page()
    app.session.login(username="test.qds.777@bk.ru", password="AnSa1991")
    app.doc.create_new_doc()
    app.session.logout()

