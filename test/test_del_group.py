import random
from model.group import Group

import allure

# from random import randrange


def test_delete_some_group(app, db, check_ui):
    with allure.step("Given a non-empty group list"):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="test"))
        old_groups = db.get_group_list()
    with allure.step("Given a randomly chosen group"):
        group = random.choice(old_groups)
    with allure.step("When I delete the chosen group from the group list"):
        app.group.delete_group_by_id(group.id)
        new_groups = db.get_group_list()
    with allure.step("Then the new group list is equal to the old list without deleted group"):
        assert len(old_groups) - 1 == app.group.count()
        old_groups.remove(group)
        #    old_groups[index:index + 1] = []
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
