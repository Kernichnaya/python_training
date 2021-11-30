from model.group import Group
from model.contact import Contact
from random import randrange
import random
import allure


def test_add_contact_into_group(app, orm, check_ui):
    with allure.step("Given a non-empty group list and a non-empty contact list"):
        if len(orm.get_group_list()) == 0:
            app.group.create(Group(name="test"))
        contact = Contact(firstname="Editcontact", lastname="Editcontact")
        groups = orm.get_group_list()
    with allure.step("Given a random contact and a random group"):
        group = random.choice(groups)
        old_contacts_list_in_group = orm.get_contacts_in_group(group)
    with allure.step(f"When I add the randomly chosen group {group} to the randomly chosen contact"):
        app.contact.add_contact_to_group(contact, group.name)
        new_contacts_list_in_group = orm.get_contacts_in_group(group)
        old_contacts_list_in_group.append(contact)
    with allure.step("Then the randomly chosen contact is in the chosen group"):
        assert sorted(old_contacts_list_in_group, key=Group.id_or_max) == sorted(new_contacts_list_in_group,
                                                                                 key=Group.id_or_max)
        if check_ui:
            assert sorted(orm.get_contacts_in_group(group), key=Group.id_or_max) == sorted(
                app.contact.get_contact_with_group(group.name), key=Group.id_or_max)
