from model.contact import Contact
import random
from random import randrange


def test_delete_some_contact(app, db, check_ui):
    if db.get_contact_list() == 0:
        app.contact.createcontact(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    content = random.choice(old_contacts)
    app.contact.delete_contact_by_id(content.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(content)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
