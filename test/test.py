# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Group1", header="Group1", footer="Group1"))
    app.session.logout()

def test_empty_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add(Contact(firstname="lv", middlname="kr", lastname="lv2", nickname="kr2", title="Title",
                            company="Company2", address="elizarovix", homephone="97-52-5", mobile="+79293713057",
                            workphone="89893585085", faxphone="89811115085", email="klobastov@gmal.com",
                            email2="Ker@gmal.com",
                            email3="rtg@gmal.com", homepage="dfgdfg", bday="14", bmonth="September",
                            byear="2000", aday="15", amonth="November", ayear="1997", address2="Adress",
                            phone2="852451285", notes="23"))
    app.session.logout()


