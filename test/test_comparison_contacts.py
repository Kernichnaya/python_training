import re
from model.contact import Contact
import allure

def test_all_info_on_home_page_and_db(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(Contact(firstname="first", homephon="87326352378", workphon="73652363281",
                                    mobile="328744653263", faxphone="87439847362"))
    with allure.step("Given a contact list from the home page"):
        contact_list_from_bd = sorted(db.get_contact_list_all(), key=Contact.id_or_max)
    with allure.step("When I get contact list from the database"):
        contact_list_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
        assert contact_list_from_home_page == contact_list_from_bd
        number_of_contacts = len(contact_list_from_bd)
    with allure.step(
            "Then the every contact of the contact list from the home page is equal to the every contact of the contact list from the database"):
        for index in range(number_of_contacts):
            bd = contact_list_from_bd[index]
            home = contact_list_from_home_page[index]
            assert home.all_phones_from_home_page == merge_phones_like_on_home_page(bd)
            assert home.all_emails_from_home_page == merge_emails_like_on_home_page(bd)
            assert home.lastname == bd.lastname
            assert home.firstname == bd.firstname
            assert home.address == bd.address


def test_phones_on_home_page(app, db):
    if db.get_group_list() == 0:
        app.contact.createcontact(Contact(firstname="test"))
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.faxphone == contact_from_edit_page.faxphone

def test_emails_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def test_address_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.address == contact_from_edit_page.address

def test_name_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobile, contact.workphone, contact.phone2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))
