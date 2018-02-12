# -*- coding: utf-8 -*-

from model.group import Group


def test_test_add_group(app):
    app.group.create(Group(name="test", group_header="test", footer="test"))


def test_add_empty_group(app):
    app.group.create(Group(name="", group_header="", footer=""))

