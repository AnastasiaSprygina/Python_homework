from model.contact import Contact

def test_edit_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(firstname="My Name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
