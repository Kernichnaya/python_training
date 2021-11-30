from model.group import Group
import random
from random import randrange
import allure


def test_modify_some_group_name(app, db, check_ui):
    with allure.step("Given a non-empty group list"):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="test"))
        old_groups = db.get_group_list()
    with allure.step("Given a randomly chosen group for modifying"):
        index = randrange(len(old_groups))
        groups = old_groups[index]
        group = Group(name="New group", header="Group2")
        group.id = old_groups[index].id
    with allure.step("When I modify the chosen group"):
        app.group.modify_group_by_id(groups.id, group)
    with allure.step("Then the new group list is equal to the old list with modified group"):
        new_groups = db.get_group_list()
        assert len(old_groups) == len(new_groups)
        old_groups[index] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == select(app.group.get_group_list(), key=Group.id_or_max)

# def test_modify_group_header(app):
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New header"))
#    assert len(old_groups) == app.group.count()
#    new_groups = app.group.get_group_list()
