from PySide6.QtGui import QTextCharFormat, QFont
from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QToolButton,
    QVBoxLayout,
)

from app.utils.image_storage import copy_image_to_data


def set_text_edit_content(text_edit: QTextEdit, content: str):
    if content.strip().lower().startswith("<!doctype html") or "<html" in content.lower():
        text_edit.setHtml(content)
    else:
        text_edit.setPlainText(content)


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
        self.setMinimumSize(600, 600)

        self.question_input = QTextEdit()
        set_text_edit_content(self.question_input, question_text)

        self.question_image_input = QLineEdit()
        self.question_image_input.setReadOnly(True)
        self.question_image_input.setText(question_image_path or "")

        self.answer_input = QTextEdit()
        set_text_edit_content(self.answer_input, answer_text)

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

        self.add_labeled_rich_text_widget(
            layout,
            "Question",
            self.question_input,
        )

        self.add_labeled_layout(
            layout,
            "Question Image",
            self.create_image_row(
                self.question_image_input,
                self.browse_question_image,
                self.clear_question_image,
            ),
        )

        self.add_labeled_rich_text_widget(
            layout,
            "Answer",
            self.answer_input,
        )

        self.add_labeled_layout(
            layout,
            "Answer Image",
            self.create_image_row(
                self.answer_image_input,
                self.browse_answer_image,
                self.clear_answer_image,
            ),
        )

        layout.addWidget(self.button_box)

        self.setLayout(layout)

        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

    def add_labeled_rich_text_widget(self, layout, label_text: str, text_edit: QTextEdit):
        layout.addWidget(QLabel(label_text))
        layout.addLayout(self.create_format_toolbar(text_edit))
        layout.addWidget(text_edit)

    @staticmethod
    def add_labeled_layout(layout, label_text: str, child_layout):
        layout.addWidget(QLabel(label_text))
        layout.addLayout(child_layout)

    def create_format_toolbar(self, text_edit: QTextEdit):
        toolbar = QHBoxLayout()

        bold_button = QToolButton()
        bold_button.setText("B")
        bold_button.setCheckable(True)
        bold_button.setStyleSheet("font-weight: bold;")
        bold_button.clicked.connect(lambda checked: self.toggle_bold(text_edit, checked))

        italic_button = QToolButton()
        italic_button.setText("I")
        italic_button.setCheckable(True)
        italic_button.setStyleSheet("font-style: italic;")
        italic_button.clicked.connect(lambda checked: self.toggle_italic(text_edit, checked))

        underline_button = QToolButton()
        underline_button.setText("U")
        underline_button.setCheckable(True)
        underline_button.setStyleSheet("text-decoration: underline;")
        underline_button.clicked.connect(lambda checked: self.toggle_underline(text_edit, checked))

        toolbar.addWidget(bold_button)
        toolbar.addWidget(italic_button)
        toolbar.addWidget(underline_button)
        toolbar.addStretch()

        return toolbar

    @staticmethod
    def merge_format(text_edit: QTextEdit, text_format: QTextCharFormat):
        cursor = text_edit.textCursor()

        if not cursor.hasSelection():
            cursor.select(cursor.SelectionType.WordUnderCursor)

        cursor.mergeCharFormat(text_format)
        text_edit.mergeCurrentCharFormat(text_format)

    def toggle_bold(self, text_edit: QTextEdit, checked: bool):
        text_format = QTextCharFormat()
        text_format.setFontWeight(QFont.Weight.Bold if checked else QFont.Weight.Normal)
        self.merge_format(text_edit, text_format)

    def toggle_italic(self, text_edit: QTextEdit, checked: bool):
        text_format = QTextCharFormat()
        text_format.setFontItalic(checked)
        self.merge_format(text_edit, text_format)

    def toggle_underline(self, text_edit: QTextEdit, checked: bool):
        text_format = QTextCharFormat()
        text_format.setFontUnderline(checked)
        self.merge_format(text_edit, text_format)

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
            "question_text": self.question_input.toHtml().strip(),
            "answer_text": self.answer_input.toHtml().strip(),
            "question_image_path": self.question_image_input.text().strip() or None,
            "answer_image_path": self.answer_image_input.text().strip() or None,
        }