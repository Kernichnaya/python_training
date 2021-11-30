from model.contact import Contact
import random
from random import randrange
import allure


def test_delete_some_contact(app, db, check_ui):
    with allure.step("Given a non-empty contact list"):
        if db.get_contact_list() == 0:
            app.contact.createcontact(Contact(firstname="test"))
        old_contacts = db.get_contact_list()
    with allure.step("Given a randomly chosen contact"):
        content = random.choice(old_contacts)
    with allure.step(f"When I delete the chosen contact {content} from the contact list"):
        app.contact.delete_contact_by_id(content.id)
    with allure.step("Then the new contact list is equal to the old list without deleted contact"):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) - 1 == len(new_contacts)
        old_contacts.remove(content)
        assert old_contacts == new_contacts
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)
