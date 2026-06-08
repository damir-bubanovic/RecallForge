from PySide6.QtWidgets import QInputDialog, QMessageBox

from app.hierarchy.hierarchy_loader import ITEM_ID_ROLE

from database.subjects import create_subject, delete_subject, update_subject
from database.topics import create_topic, delete_topic, update_topic


def run_action(parent, action, reload_callback):
    try:
        action()
        reload_callback()
    except Exception as error:
        QMessageBox.warning(parent, "Error", str(error))

def add_subject(parent, reload_callback):
    name, ok = QInputDialog.getText(parent, "Add Subject", "Subject name:")

    if not ok:
        return

    run_action(
        parent,
        lambda: create_subject(name),
        reload_callback,
    )


def rename_subject(parent, item, reload_callback):
    subject_id = item.data(0, ITEM_ID_ROLE)
    current_name = item.text(0)

    new_name, ok = QInputDialog.getText(
        parent,
        "Rename Subject",
        "New subject name:",
        text=current_name,
    )

    if not ok:
        return

    run_action(
        parent,
        lambda: update_subject(subject_id, new_name),
        reload_callback,
    )


def remove_subject(parent, item, reload_callback):
    subject_id = item.data(0, ITEM_ID_ROLE)
    subject_name = item.text(0)

    confirmation = QMessageBox.question(
        parent,
        "Delete Subject",
        f"Delete subject '{subject_name}' and all its topics?",
    )

    if confirmation != QMessageBox.StandardButton.Yes:
        return

    run_action(
        parent,
        lambda: delete_subject(subject_id),
        reload_callback,
    )


def add_topic(parent, subject_item, reload_callback):
    subject_id = subject_item.data(0, ITEM_ID_ROLE)

    name, ok = QInputDialog.getText(parent, "Add Topic", "Topic name:")

    if not ok:
        return

    run_action(
        parent,
        lambda: create_topic(subject_id, name),
        reload_callback,
    )


def rename_topic(parent, item, reload_callback):
    topic_id = item.data(0, ITEM_ID_ROLE)
    current_name = item.text(0)

    new_name, ok = QInputDialog.getText(
        parent,
        "Rename Topic",
        "New topic name:",
        text=current_name,
    )

    if not ok:
        return

    run_action(
        parent,
        lambda: update_topic(topic_id, new_name),
        reload_callback,
    )


def remove_topic(parent, item, reload_callback):
    topic_id = item.data(0, ITEM_ID_ROLE)
    topic_name = item.text(0)

    confirmation = QMessageBox.question(
        parent,
        "Delete Topic",
        f"Delete topic '{topic_name}'?",
    )

    if confirmation != QMessageBox.StandardButton.Yes:
        return

    run_action(
        parent,
        lambda: delete_topic(topic_id),
        reload_callback,
    )