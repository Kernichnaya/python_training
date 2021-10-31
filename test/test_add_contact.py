from model.contact import Contact
import random
import string
import pytest


def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


def random_number(maxlen):
    symbol = string.digits
    return "7".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


testdatacontact = [Contact(firstname="", middlename="", lastname="", nickname="", company="", address="",
                           homephone="", mobile="", faxphone="")] + [
                      Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                              lastname=random_string("lastname", 10),
                              nickname=random_string("nickname", 10), company=random_string("company", 10),
                              address=random_string("address", 10),
                              homephone=random_number(11), mobile=random_number(11), faxphone=random_number(11))
                      for i in range(3)
                  ]


# for firstname in ["", random_string("firstname", 10)]
# for middlename in ["", random_string("middlename", 20)]
# for lastname in ["", random_string("lastname", 20)]
# ]


@pytest.mark.parametrize("contact", testdatacontact, ids=[repr(x) for x in testdatacontact])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.createcon(contact)
    assert len(old_contacts) + 1 == app.contact.countcon()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
