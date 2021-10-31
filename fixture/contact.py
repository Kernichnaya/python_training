from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

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
        self.change_field_value_con("work", contact.workphone)  # contact.work
        self.change_field_value_con("phone2", contact.faxphone)  # contact.fax
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

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_start_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_start_page()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_start_page()
        wd.find_elements_by_xpath('//img[@title="Edit"]')[index].click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.open_start_page()
        self.contact_cache = None

    def countcon(self):
        wd = self.app.wd
        self.open_start_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_start_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_start_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_start_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_xpath("td")
                lastname = element.find_element_by_xpath("td[2]").text
                firstname = element.find_element_by_xpath("td[3]").text
                address = element.find_element_by_xpath("td[4]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id, address=address,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        faxphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")

        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, workphone=workphone,
                       mobile=mobile, phone2=faxphone, address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        faxphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone,
                       mobile=mobile, phone2=faxphone)
