from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTreeWidgetItem

from database.subjects import get_subjects
from database.topics import get_topics_by_subject


ITEM_TYPE_ROLE = Qt.ItemDataRole.UserRole
ITEM_ID_ROLE = Qt.ItemDataRole.UserRole + 1


def load_hierarchy(tree):
    tree.clear()

    subjects = get_subjects()

    for subject in subjects:
        subject_item = QTreeWidgetItem([subject["name"]])
        subject_item.setData(0, ITEM_TYPE_ROLE, "subject")
        subject_item.setData(0, ITEM_ID_ROLE, subject["id"])

        topics = get_topics_by_subject(subject["id"])

        for topic in topics:
            topic_item = QTreeWidgetItem([topic["name"]])
            topic_item.setData(0, ITEM_TYPE_ROLE, "topic")
            topic_item.setData(0, ITEM_ID_ROLE, topic["id"])
            subject_item.addChild(topic_item)

        tree.addTopLevelItem(subject_item)

    tree.expandAll()