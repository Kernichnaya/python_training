from model.group import Group
from model.contact import Contact
from random import randrange
import random


def test_add_contact_in_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_contact_list()) == 0:
        app.contact.createcontact(Contact(firstname="firstname", homephone="8941115378", workphone="7657225281",
                                          mobile="77785553263", phone2="52527462"))
    old_contact_in_db = db.count_contact_in_group()
    if len(app.contact.get_contact_list_in_none_group()) == 0:
        app.contact.createcontact(Contact(firstname="random", homephone="8941115378", workphone="7782752476",
                                          mobile="7782258476", phone2="7782752112"))
        app.contact.open_none_group()
    old_contacts = app.contact.get_contact_list_in_none_group()
    index = randrange(len(old_contacts))
    contacts = old_contacts[index]
    app.contact.add_in_group(contacts.id)
    new_contact_in_db = db.count_contact_in_group()
    assert old_contact_in_db + 1 == new_contact_in_db
