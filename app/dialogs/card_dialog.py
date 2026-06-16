from PySide6.QtGui import QTextCharFormat, QTextImageFormat, QTextListFormat, QFont, QImageReader
from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QTextEdit,
    QToolButton,
    QVBoxLayout,
)

from app.utils.image_storage import copy_image_to_data


FONT_SIZES = [18, 20, 22, 24, 26, 28, 32]
INLINE_IMAGE_MAX_WIDTH = 520


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
    ):
        super().__init__(parent)

        self.setWindowTitle(title)
        self.setMinimumSize(600, 600)

        self.question_input = QTextEdit()
        set_text_edit_content(self.question_input, question_text)

        self.answer_input = QTextEdit()
        set_text_edit_content(self.answer_input, answer_text)

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

        self.add_labeled_rich_text_widget(
            layout,
            "Answer",
            self.answer_input,
        )

        layout.addWidget(self.button_box)

        self.setLayout(layout)

        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

    def add_labeled_rich_text_widget(self, layout, label_text: str, text_edit: QTextEdit):
        layout.addWidget(QLabel(label_text))
        layout.addLayout(self.create_format_toolbar(text_edit))
        layout.addWidget(text_edit)

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

        bullet_button = QToolButton()
        bullet_button.setText("• List")
        bullet_button.clicked.connect(
            lambda: self.apply_list(text_edit, QTextListFormat.Style.ListDisc)
        )

        numbered_button = QToolButton()
        numbered_button.setText("1. List")
        numbered_button.clicked.connect(
            lambda: self.apply_list(text_edit, QTextListFormat.Style.ListDecimal)
        )

        font_size_dropdown = QComboBox()
        for size in FONT_SIZES:
            font_size_dropdown.addItem(f"{size}px", size)

        font_size_dropdown.setCurrentText("18px")
        font_size_dropdown.currentIndexChanged.connect(
            lambda index: self.apply_font_size(
                text_edit,
                font_size_dropdown.itemData(index),
            )
        )

        insert_image_button = QToolButton()
        insert_image_button.setText("Image")
        insert_image_button.clicked.connect(
            lambda: self.insert_inline_image(text_edit)
        )

        toolbar.addWidget(bold_button)
        toolbar.addWidget(italic_button)
        toolbar.addWidget(underline_button)
        toolbar.addWidget(bullet_button)
        toolbar.addWidget(numbered_button)
        toolbar.addWidget(QLabel("Size"))
        toolbar.addWidget(font_size_dropdown)
        toolbar.addWidget(insert_image_button)
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

    def apply_font_size(self, text_edit: QTextEdit, size: int):
        text_format = QTextCharFormat()
        text_format.setFontPointSize(size)
        self.merge_format(text_edit, text_format)

    @staticmethod
    def apply_list(text_edit: QTextEdit, list_style: QTextListFormat.Style):
        cursor = text_edit.textCursor()
        cursor.beginEditBlock()

        list_format = QTextListFormat()
        list_format.setStyle(list_style)

        cursor.createList(list_format)
        cursor.endEditBlock()

        text_edit.setFocus()

    def insert_inline_image(self, text_edit: QTextEdit):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Insert Image",
            "",
            "Images (*.png *.jpg *.jpeg *.webp *.svg)"
        )

        if not file_path:
            return

        copied_path = copy_image_to_data(file_path)

        image_reader = QImageReader(copied_path)
        image_size = image_reader.size()

        image_format = QTextImageFormat()
        image_format.setName(copied_path)

        if image_size.isValid():
            available_width = max(200, text_edit.viewport().width() - 40)
            display_width = min(
                image_size.width(),
                available_width,
                INLINE_IMAGE_MAX_WIDTH,
            )
            image_format.setWidth(display_width)

        cursor = text_edit.textCursor()
        cursor.insertImage(image_format)
        cursor.insertBlock()

        text_edit.setFocus()

    def get_data(self):
        return {
            "question_text": self.question_input.toHtml().strip(),
            "answer_text": self.answer_input.toHtml().strip(),
        }