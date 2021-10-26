from selenium.webdriver.support.select import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_start_page(self):
        wd = self.app.wd
        if not len(wd.find_elements_by_name("//input[@value='Delete']")) > 0:
            wd.find_element_by_link_text("home").click()

    def open_contact_add(self):
        wd = self.app.wd
        if not len(wd.find_elements_by_link_text("Edit / add address book entry")) > 0:
            wd.find_element_by_link_text("add new").click()

    def change_field_value_con(self, field_data, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_data).click()
            wd.find_element_by_name(field_data).clear()
            wd.find_element_by_name(field_data).send_keys(text)

    def change_field_select_con(self, field_select, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_select).click()
            Select(wd.find_element_by_name(field_select)).select_by_visible_text(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value_con("firstname", contact.firstname)
        self.change_field_value_con("middlename", contact.middlename)
        self.change_field_value_con("lastname", contact.lastname)
        self.change_field_value_con("nickname", contact.nickname)
        self.change_field_value_con("title", contact.title)
        self.change_field_value_con("company", contact.company)
        self.change_field_value_con("address", contact.address)
        self.change_field_value_con("home", contact.homephone)  # contact.home
        self.change_field_value_con("mobile", contact.mobile)
        self.change_field_value_con("mobile", contact.workphone)  # contact.work
        self.change_field_value_con("fax", contact.faxphone)  # contact.fax
        self.change_field_value_con("email", contact.email)
        self.change_field_value_con("email2", contact.email2)
        self.change_field_value_con("email3", contact.email3)
        self.change_field_value_con("email3", contact.homepage)
        self.change_field_select_con("bday", contact.bday)
        self.change_field_select_con("bmonth", contact.bmonth)
        self.change_field_value_con("byear", contact.byear)
        self.change_field_select_con("aday", contact.aday)
        self.change_field_select_con("amonth", contact.amonth)
        self.change_field_value_con("ayear", contact.ayear)
        self.change_field_value_con("address2", contact.address2)
        self.change_field_value_con("phone2", contact.phone2)
        self.change_field_value_con("notes", contact.notes)

    def createcon(self, contact):
        wd = self.app.wd
        self.open_start_page()
        self.open_contact_add()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.open_start_page()
        self.contact_cache = None

    def selected_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_start_page()
        self.selected_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_start_page()
        self.contact_cache = None

    def modify_first_contact(self, modify_first_contact):
        wd = self.app.wd
        self.open_start_page()
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        self.fill_contact_form(modify_first_contact)
        wd.find_element_by_name("update").click()
        self.open_start_page()
        self.contact_cache = None

    def countcon(self):
        wd = self.app.wd
        self.open_start_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_start_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                firstname = element.find_element_by_xpath(".//td[3]").text
                lastname = element.find_element_by_xpath(".//td[2]").text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)
