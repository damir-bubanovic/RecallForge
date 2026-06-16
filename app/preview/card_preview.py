from PySide6.QtWidgets import QLabel, QTextEdit, QVBoxLayout, QWidget

from app.styles.font_sizes import (
    FONT_SIZE_PANEL_TITLE,
    FONT_SIZE_SMALL,
    font_size_px,
)


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
        self.question_text.setMinimumHeight(220)

        self.answer_label = QLabel("Answer")
        self.answer_label.setStyleSheet(
            f"{font_size_px(FONT_SIZE_SMALL)} font-weight: bold;"
        )

        self.answer_text = QTextEdit()
        self.answer_text.setReadOnly(True)
        self.answer_text.setMinimumHeight(220)

        self.setup_ui()
        self.clear_preview()

    def setup_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(self.title_label)

        layout.addWidget(self.question_label)
        layout.addWidget(self.question_text)

        layout.addWidget(self.answer_label)
        layout.addWidget(self.answer_text)

        self.setLayout(layout)

    def show_card(
        self,
        question: str,
        answer: str,
    ):
        self.question_text.setHtml(question)
        self.answer_text.setHtml(answer)

    def clear_preview(self):
        self.question_text.clear()
        self.answer_text.clear()