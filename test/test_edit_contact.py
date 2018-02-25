from model.contact import Contact
from random import randrange

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="test", middlename="test", lastname="test", nickname="test", title="test", company="test", address="test", home="test", mobile="test", work="test", fax="test", email="test", email2="test", email3="test", homepage="test", byear="2018")
    app.contact.edit_contact_by_index(index, contact)
    contact.id = old_contacts[index].id
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



