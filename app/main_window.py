from PySide6.QtWidgets import (
    QHBoxLayout,
    QInputDialog,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from database.subjects import (
    create_subject,
    delete_subject,
    get_subjects,
    update_subject,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RecallForge")
        self.setMinimumSize(900, 600)

        self.subjects_list = QListWidget()
        self.content_label = QLabel("Select a subject")
        self.content_label.setStyleSheet("font-size: 24px;")

        self.setup_ui()
        self.load_subjects()

    def setup_ui(self):
        main_layout = QHBoxLayout()

        sidebar_layout = QVBoxLayout()

        title_label = QLabel("Subjects")
        title_label.setStyleSheet("font-size: 20px; font-weight: bold;")

        add_button = QPushButton("Add Subject")
        rename_button = QPushButton("Rename Subject")
        delete_button = QPushButton("Delete Subject")

        add_button.clicked.connect(self.add_subject)
        rename_button.clicked.connect(self.rename_subject)
        delete_button.clicked.connect(self.remove_subject)

        self.subjects_list.itemClicked.connect(self.subject_selected)

        sidebar_layout.addWidget(title_label)
        sidebar_layout.addWidget(self.subjects_list)
        sidebar_layout.addWidget(add_button)
        sidebar_layout.addWidget(rename_button)
        sidebar_layout.addWidget(delete_button)

        sidebar_widget = QWidget()
        sidebar_widget.setLayout(sidebar_layout)
        sidebar_widget.setFixedWidth(250)

        content_layout = QVBoxLayout()
        content_layout.addWidget(self.content_label)

        content_widget = QWidget()
        content_widget.setLayout(content_layout)

        main_layout.addWidget(sidebar_widget)
        main_layout.addWidget(content_widget)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)

    def load_subjects(self):
        self.subjects_list.clear()

        subjects = get_subjects()

        for subject in subjects:
            item = QListWidgetItem(subject["name"])
            item.setData(1000, subject["id"])
            self.subjects_list.addItem(item)

    def get_selected_subject_item(self):
        return self.subjects_list.currentItem()

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
            self.load_subjects()
        except Exception as error:
            QMessageBox.warning(self, "Error", str(error))

    def rename_subject(self):
        selected_item = self.get_selected_subject_item()

        if selected_item is None:
            QMessageBox.information(self, "No Subject Selected", "Please select a subject first.")
            return

        subject_id = selected_item.data(1000)
        current_name = selected_item.text()

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
            self.load_subjects()
        except Exception as error:
            QMessageBox.warning(self, "Error", str(error))

    def remove_subject(self):
        selected_item = self.get_selected_subject_item()

        if selected_item is None:
            QMessageBox.information(self, "No Subject Selected", "Please select a subject first.")
            return

        subject_id = selected_item.data(1000)
        subject_name = selected_item.text()

        confirmation = QMessageBox.question(
            self,
            "Delete Subject",
            f"Delete subject '{subject_name}'?",
        )

        if confirmation != QMessageBox.StandardButton.Yes:
            return

        try:
            delete_subject(subject_id)
            self.content_label.setText("Select a subject")
            self.load_subjects()
        except Exception as error:
            QMessageBox.warning(self, "Error", str(error))

    def subject_selected(self, item):
        subject_name = item.text()
        self.content_label.setText(f"Selected subject: {subject_name}")