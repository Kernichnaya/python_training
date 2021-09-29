# -*- coding: utf-8 -*-
from select import select

from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from selenium.webdriver.support.select import Select
from contacts import Contacts
from group import Group

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def create_group(self, wd, group):
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_xpath("//body").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def return_to_groups_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def open_contacts_add(self, wd):
        wd.find_element_by_link_text("add new").click()

    def contacts_add(self, wd, contacts):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys(contacts.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").send_keys(contacts.middlname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").send_keys(contacts.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").send_keys(contacts.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").send_keys(contacts.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").send_keys(contacts.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").send_keys(contacts.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contacts.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").send_keys(contacts.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").send_keys(contacts.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").send_keys(contacts.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").send_keys(contacts.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").send_keys(contacts.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").send_keys(contacts.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").send_keys(contacts.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contacts.bday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contacts.bmonth)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").send_keys(contacts.byear)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contacts.aday)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contacts.amonth)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").send_keys(contacts.ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").send_keys(contacts.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").send_keys("phone2")
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").send_keys(contacts.notes)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_group(wd, Group(name="Group1", header="Group1", footer="Group1"))
        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_empty_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_group(wd, Group(name="", header="", footer=""))
        self.return_to_groups_page(wd)
        self.logout(wd)


    def test_create_add_new(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_contacts_add(wd)
        self.contacts_add(wd, Contacts(firstname="lv", middlname="kr", lastname="lv2", nickname="kr2", title="Title", company="Company2", address="elizarovix",  home="home", mobile="+79293713057",
                     work="wrk)", fax="fax", email="klobastov@gmal.com", email2="Ker@fyhd.ffv", email3="rtg@ds.dff", homepage="dfgdfg", bday="14", bmonth="September", byear="2000",
                     aday="15", amonth="November", ayear="1997",  address2="Adress", notes="23"))
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
