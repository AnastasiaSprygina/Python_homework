# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "
    return prefix + " ".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname=" ", middlename=" ", lastname=" ", nickname=" ", title=" ", company=" ", address=" ", home=" ", mobile=" ", work=" ", fax=" ",
                    email=" ", email2=" ", email3=" ", homepage=" ", byear=" ")] + [Contact(firstname=random_string("testtest", 10), middlename=random_string("testtest", 10), lastname=random_string("testtest", 10), nickname=random_string("testtest", 10), title=random_string("testtest", 10), company=random_string("testtest", 10), address=random_string("testtest", 10), home=random_string("testtest", 10), mobile=random_string("testtest", 10), work=random_string("testtest", 10), fax=random_string("testtest", 10), email=random_string("testtest", 10), email2=random_string("testtest", 10),
                    email3=random_string("testtest", 10), homepage=random_string("testtest", 10),
                    byear=random_string("testtest", 10))
                    for i in range(5)]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])

def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


