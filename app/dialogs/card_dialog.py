from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
)

from app.utils.image_storage import copy_image_to_data


class CardDialog(QDialog):
    def __init__(
        self,
        parent=None,
        title="Card",
        question_text="",
        answer_text="",
        question_image_path=None,
        answer_image_path=None,
    ):
        super().__init__(parent)

        self.setWindowTitle(title)
        self.setMinimumSize(600, 550)

        self.question_input = QTextEdit()
        self.question_input.setPlainText(question_text)

        self.question_image_input = QLineEdit()
        self.question_image_input.setReadOnly(True)
        self.question_image_input.setText(question_image_path or "")

        self.answer_input = QTextEdit()
        self.answer_input.setPlainText(answer_text)

        self.answer_image_input = QLineEdit()
        self.answer_image_input.setReadOnly(True)
        self.answer_image_input.setText(answer_image_path or "")

        self.button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save
            | QDialogButtonBox.StandardButton.Cancel
        )

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Question"))
        layout.addWidget(self.question_input)

        layout.addWidget(QLabel("Question Image"))
        layout.addLayout(
            self.create_image_row(
                self.question_image_input,
                self.browse_question_image,
                self.clear_question_image,
            )
        )

        layout.addWidget(QLabel("Answer"))
        layout.addWidget(self.answer_input)

        layout.addWidget(QLabel("Answer Image"))
        layout.addLayout(
            self.create_image_row(
                self.answer_image_input,
                self.browse_answer_image,
                self.clear_answer_image,
            )
        )

        layout.addWidget(self.button_box)

        self.setLayout(layout)

        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

    @staticmethod
    def create_image_row(line_edit, browse_callback, clear_callback):
        row = QHBoxLayout()

        browse_button = QPushButton("Browse")
        clear_button = QPushButton("Clear")

        browse_button.clicked.connect(browse_callback)
        clear_button.clicked.connect(clear_callback)

        row.addWidget(line_edit)
        row.addWidget(browse_button)
        row.addWidget(clear_button)

        return row

    def browse_question_image(self):
        self.select_image(self.question_image_input)

    def browse_answer_image(self):
        self.select_image(self.answer_image_input)

    def clear_question_image(self):
        self.question_image_input.clear()

    def clear_answer_image(self):
        self.answer_image_input.clear()

    def select_image(self, target_input):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Image",
            "",
            "Images (*.png *.jpg *.jpeg *.webp *.svg)"
        )

        if not file_path:
            return

        copied_path = copy_image_to_data(file_path)
        target_input.setText(copied_path)

    def get_data(self):
        return {
            "question_text": self.question_input.toPlainText().strip(),
            "answer_text": self.answer_input.toPlainText().strip(),
            "question_image_path": self.question_image_input.text().strip() or None,
            "answer_image_path": self.answer_image_input.text().strip() or None,
        }