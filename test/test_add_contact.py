from model.contact import Contact
import allure

def test_add_contact(app, json_contacts, db, check_ui):
    contact = json_contacts
    with allure.step("Given a contact list"):
        old_contacts = db.get_contact_list()
    with allure.step(f"When I add a contact {contact} to the contact list"):
        app.contact.createcontact(contact)
    with allure.step("Then the new contact list is equal to the old list with the added contact"):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) + 1 == len(new_contacts)
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)
