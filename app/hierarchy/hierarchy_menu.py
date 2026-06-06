from PySide6.QtWidgets import QMenu

from app.hierarchy.hierarchy_actions import (
    add_subject,
    add_topic,
    remove_subject,
    remove_topic,
    rename_subject,
    rename_topic,
)
from app.hierarchy.hierarchy_loader import ITEM_TYPE_ROLE


def open_context_menu(parent, tree, position, reload_callback):
    item = tree.itemAt(position)

    menu = QMenu(parent)

    if item is None:
        add_subject_action = menu.addAction("Add Subject")

        selected_action = menu.exec(tree.viewport().mapToGlobal(position))

        if selected_action == add_subject_action:
            add_subject(parent, reload_callback)

        return

    item_type = item.data(0, ITEM_TYPE_ROLE)

    if item_type == "subject":
        add_topic_action = menu.addAction("Add Topic")
        rename_subject_action = menu.addAction("Rename Subject")
        delete_subject_action = menu.addAction("Delete Subject")

        selected_action = menu.exec(tree.viewport().mapToGlobal(position))

        if selected_action == add_topic_action:
            add_topic(parent, item, reload_callback)
        elif selected_action == rename_subject_action:
            rename_subject(parent, item, reload_callback)
        elif selected_action == delete_subject_action:
            remove_subject(parent, item, reload_callback)

    elif item_type == "topic":
        rename_topic_action = menu.addAction("Rename Topic")
        delete_topic_action = menu.addAction("Delete Topic")

        selected_action = menu.exec(tree.viewport().mapToGlobal(position))

        if selected_action == rename_topic_action:
            rename_topic(parent, item, reload_callback)
        elif selected_action == delete_topic_action:
            remove_topic(parent, item, reload_callback)