from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QInputDialog,
    QMenu,
    QMessageBox,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)

from database.subjects import (
    create_subject,
    delete_subject,
    get_subjects,
    update_subject,
)

from database.topics import (
    create_topic,
    delete_topic,
    get_topics_by_subject,
    update_topic,
)


ITEM_TYPE_ROLE = Qt.ItemDataRole.UserRole
ITEM_ID_ROLE = Qt.ItemDataRole.UserRole + 1


class HierarchyPanel(QWidget):
    topic_selected_signal = Signal(int, str)

    def __init__(self):
        super().__init__()

        self.tree = QTreeWidget()
        self.tree.setHeaderLabel("Subjects / Topics")
        self.tree.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        self.setup_ui()
        self.load_hierarchy()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(self.tree)
        self.setLayout(layout)
        self.setFixedWidth(300)

        self.tree.customContextMenuRequested.connect(self.open_context_menu)
        self.tree.itemClicked.connect(self.handle_item_clicked)

    def load_hierarchy(self):
        self.tree.clear()

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

            self.tree.addTopLevelItem(subject_item)

        self.tree.expandAll()

    def open_context_menu(self, position):
        item = self.tree.itemAt(position)

        menu = QMenu(self)

        if item is None:
            add_subject_action = menu.addAction("Add Subject")
            selected_action = menu.exec(self.tree.viewport().mapToGlobal(position))

            if selected_action == add_subject_action:
                self.add_subject()

            return

        item_type = item.data(0, ITEM_TYPE_ROLE)

        if item_type == "subject":
            add_topic_action = menu.addAction("Add Topic")
            rename_subject_action = menu.addAction("Rename Subject")
            delete_subject_action = menu.addAction("Delete Subject")

            selected_action = menu.exec(self.tree.viewport().mapToGlobal(position))

            if selected_action == add_topic_action:
                self.add_topic(item)
            elif selected_action == rename_subject_action:
                self.rename_subject(item)
            elif selected_action == delete_subject_action:
                self.remove_subject(item)

        elif item_type == "topic":
            rename_topic_action = menu.addAction("Rename Topic")
            delete_topic_action = menu.addAction("Delete Topic")

            selected_action = menu.exec(self.tree.viewport().mapToGlobal(position))

            if selected_action == rename_topic_action:
                self.rename_topic(item)
            elif selected_action == delete_topic_action:
                self.remove_topic(item)

    def add_subject(self):
        name, ok = QInputDialog.getText(
            self,
            "Add Subject",
            "Subject name:",
        )

        if not ok:
            return

        try:
            create_subject(name)
            self.load_hierarchy()
        except Exception as error:
            QMessageBox.warning(self, "Error", str(error))

    def rename_subject(self, item):
        subject_id = item.data(0, ITEM_ID_ROLE)
        current_name = item.text(0)

        new_name, ok = QInputDialog.getText(
            self,
            "Rename Subject",
            "New subject name:",
            text=current_name,
        )

        if not ok:
            return

        try:
            update_subject(subject_id, new_name)
            self.load_hierarchy()
        except Exception as error:
            QMessageBox.warning(self, "Error", str(error))

    def remove_subject(self, item):
        subject_id = item.data(0, ITEM_ID_ROLE)
        subject_name = item.text(0)

        confirmation = QMessageBox.question(
            self,
            "Delete Subject",
            f"Delete subject '{subject_name}' and all its topics?",
        )

        if confirmation != QMessageBox.StandardButton.Yes:
            return

        try:
            delete_subject(subject_id)
            self.load_hierarchy()
        except Exception as error:
            QMessageBox.warning(self, "Error", str(error))

    def add_topic(self, subject_item):
        subject_id = subject_item.data(0, ITEM_ID_ROLE)

        name, ok = QInputDialog.getText(
            self,
            "Add Topic",
            "Topic name:",
        )

        if not ok:
            return

        try:
            create_topic(subject_id, name)
            self.load_hierarchy()
        except Exception as error:
            QMessageBox.warning(self, "Error", str(error))

    def rename_topic(self, item):
        topic_id = item.data(0, ITEM_ID_ROLE)
        current_name = item.text(0)

        new_name, ok = QInputDialog.getText(
            self,
            "Rename Topic",
            "New topic name:",
            text=current_name,
        )

        if not ok:
            return

        try:
            update_topic(topic_id, new_name)
            self.load_hierarchy()
        except Exception as error:
            QMessageBox.warning(self, "Error", str(error))

    def remove_topic(self, item):
        topic_id = item.data(0, ITEM_ID_ROLE)
        topic_name = item.text(0)

        confirmation = QMessageBox.question(
            self,
            "Delete Topic",
            f"Delete topic '{topic_name}'?",
        )

        if confirmation != QMessageBox.StandardButton.Yes:
            return

        try:
            delete_topic(topic_id)
            self.load_hierarchy()
        except Exception as error:
            QMessageBox.warning(self, "Error", str(error))

    def handle_item_clicked(self, item):
        item_type = item.data(0, ITEM_TYPE_ROLE)

        if item_type != "topic":
            return

        topic_id = item.data(0, ITEM_ID_ROLE)
        topic_name = item.text(0)

        self.topic_selected_signal.emit(topic_id, topic_name)