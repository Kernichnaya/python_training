# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Group1", header="Group1", footer="Group1"))


def test_empty_add_group(app):
    app.group.create(Group(name="", header="", footer=""))


