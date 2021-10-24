from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.countcon() == 0:
        app.contact.createcon(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Иванов", middlename="Иван", lastname="Иванович", nickname="ИИИ", title="Title 2",
                      company="Company", address="Ленина", homephone="8-800-55", mobile="+88005553535",
                      workphone="89893577777", faxphone="89811115085", email="ivanov@gmal.com",
                      email2="ivanov2@gmal.com",
                      email3="ivanov3@gmal.com", homepage="qwerty", bday="15", bmonth="September",
                      byear="2001", aday="16", amonth="November", ayear="1998", address2="Adress2",
                      phone2="852451285", notes="24")
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
