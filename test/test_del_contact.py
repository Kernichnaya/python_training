from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.countcon() == 0:
        app.contact.createcon(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    assert len(old_contacts) - 1 == app.contact.countcon()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
