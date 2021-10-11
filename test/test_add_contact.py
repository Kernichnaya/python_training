from model.contact import Contact


def test_add_contact(app):
    app.contact.createcon(Contact(firstname="lv", middlename="kr", lastname="lv2", nickname="kr2", title="Title",
                                  company="Company2", address="elizarovix", homephone="97-52-5", mobile="+79293713057",
                                  workphone="89893585085", faxphone="89811115085", email="klobastov@gmal.com",
                                  email2="Ker@gmal.com",
                                  email3="rtg@gmal.com", homepage="dfgdfg", bday="14", bmonth="September",
                                  byear="2000", aday="15", amonth="November", ayear="1997", address2="Adress",
                                  phone2="852451285", notes="23"))
