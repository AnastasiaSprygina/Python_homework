# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.Application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="test", group_header="test", footer="test"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", group_header="", footer=""))
    app.logout()
