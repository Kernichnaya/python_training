from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.countcon() == 0:
        app.contact.createcon(Contact(firstname="test"))
    app.contact.delete_first_contact()
