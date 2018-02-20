# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(Contact(firstname="test", middlename="test", lastname="test", nickname="test", title="test", company="test", address="test", home="test", mobile="test", work="test", fax="test", email="test", email2="test", email3="test", homepage="test", byear="2018"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


