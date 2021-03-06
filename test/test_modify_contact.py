from model.contact import Contact
from random import randrange
import allure


def test_modify_some_contact_name(app, db, check_ui):
    with allure.step("Given a non-empty contact list"):
        if db.get_contact_list() == 0:
            app.contact.createcontact(Contact(firstname="test"))
        old_contacts = db.get_contact_list()
        index = randrange(len(old_contacts))
        contacts = old_contacts[index]
    with allure.step("Given a contact for modifying"):
        contact = Contact(firstname="Иванов", middlename="Иван", lastname="Иванович", nickname="ИИИ", title="Title 2",
                          company="Company", address="Ленина", homephone="homephone880055", mobile="mobile88005553535",
                          workphone="workphone89893577777", faxphone="faxphone89811115085", email="ivanov@gmal.com",
                          email2="ivanov2@gmal.com",
                          email3="ivanov3@gmal.com", homepage="qwerty", bday="15", bmonth="September",
                          byear="2001", aday="16", amonth="November", ayear="1998", address2="Adress2",
                          phone2="852451285", notes="24")
        contact.id = old_contacts[index].id
    with allure.step("When I modify the chosen contact"):
        app.contact.modify_contact_by_id(contacts.id, contact)
    with allure.step("Then the new contact list is equal to the old list with modified contact"):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) == len(new_contacts)
        old_contacts[index] = contact
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)
