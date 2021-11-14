from model.group import Group
from random import randrange
from model.contact import Contact
from test import test_add_contact_in_group
import random


def test_del_contact_in_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_contact_in_db = db.count_contact_in_group()
    if len(app.contact.get_contact_list_in_group()) == 0:
        old_contacts = app.contact.get_contact_list_in_none_group()
        index = randrange(len(old_contacts))
        contacts = old_contacts[index]
        app.contact.add_in_group(contacts.id)
        app.contact.open_none_group()
    old_contacts = app.contact.get_contact_list_in_group()
    index = randrange(len(old_contacts))
    contacts = old_contacts[index]
    app.contact.del_in_group_by_id(contacts.id)
    new_contact_in_db = db.count_contact_in_group()
    assert old_contact_in_db - 1 == new_contact_in_db
