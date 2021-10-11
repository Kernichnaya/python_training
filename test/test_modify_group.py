from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New group", header="Group2"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New header"))
