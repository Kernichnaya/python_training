# -*- coding: utf-8 -*-
from model.group import Group
import allure
"""import pytest
from data.groups import testdata
from data.add_group import constant as testdata
@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])"""


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    with allure.step("Given a group list"):
        old_groups = db.get_group_list()
    with allure.step(f"When I add a group {group} to the list"):
        app.group.create(group)
        #    assert len(old_groups) + 1 == app.group.count()
    with allure.step(f'Then the new group list is equal to the old list with the added group'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

"""def test_empty_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="Group1", header="Group1", footer="Group1")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)"""
