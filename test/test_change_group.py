from model.group import Group


def test_change_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.change(Group(name="Group2", header="Group2", footer="Group3"))
    app.session.logout()
