from model.group import Group
from random import randrange

def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New group")
    app.group.edit_group_by_index(index, group)
    group.id = old_groups[index].id
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_first_group_header(app):
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(group_header="New group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
