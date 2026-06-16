from PySide6.QtWidgets import QLabel, QTextEdit, QVBoxLayout, QWidget

from app.styles.font_sizes import (
    FONT_SIZE_PANEL_TITLE,
    FONT_SIZE_SMALL,
    font_size_px,
)
from app.widgets.image_viewer import ImageViewer


class CardPreview(QWidget):
    def __init__(self):
        super().__init__()

        self.title_label = QLabel("Card Preview")
        self.title_label.setStyleSheet(
            f"{font_size_px(FONT_SIZE_PANEL_TITLE)} font-weight: bold;"
        )

        self.question_label = QLabel("Question")
        self.question_label.setStyleSheet(
            f"{font_size_px(FONT_SIZE_SMALL)} font-weight: bold;"
        )

        self.question_text = QTextEdit()
        self.question_text.setReadOnly(True)
        self.question_text.setMinimumHeight(140)

        self.question_image_viewer = ImageViewer(width=300, height=180)

        self.answer_label = QLabel("Answer")
        self.answer_label.setStyleSheet(
            f"{font_size_px(FONT_SIZE_SMALL)} font-weight: bold;"
        )

        self.answer_text = QTextEdit()
        self.answer_text.setReadOnly(True)
        self.answer_text.setMinimumHeight(140)

        self.answer_image_viewer = ImageViewer(width=300, height=180)

        self.setup_ui()
        self.clear_preview()

    def setup_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(self.title_label)

        layout.addWidget(self.question_label)
        layout.addWidget(self.question_text)
        layout.addWidget(self.question_image_viewer)

        layout.addWidget(self.answer_label)
        layout.addWidget(self.answer_text)
        layout.addWidget(self.answer_image_viewer)

        self.setLayout(layout)

    def show_card(
        self,
        question: str,
        answer: str,
        question_image_path: str | None = None,
        answer_image_path: str | None = None,
    ):
        self.question_text.setHtml(question)
        self.answer_text.setHtml(answer)

        self.question_image_viewer.show_image(question_image_path)
        self.answer_image_viewer.show_image(answer_image_path)

    def clear_preview(self):
        self.question_text.clear()
        self.answer_text.clear()

        self.question_image_viewer.clear()
        self.answer_image_viewer.clear()