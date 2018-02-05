# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application2 import Application2

@pytest.fixture
def app(request):
    fixture = Application2()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_test_add_contact(app):
    app.login(name="admin", password="secret")
    app.create_contact(Contact(firstname="test", middlename="test", lastname="test", nickname="test", title="test", company="test", address="test", home="test", mobile="test", work="test", fax="test", email="test", email2="test", email3="test", homepage="test", byear="2018"))
    app.logout()



