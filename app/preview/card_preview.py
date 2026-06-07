from PySide6.QtWidgets import QLabel, QTextEdit, QVBoxLayout, QWidget


class CardPreview(QWidget):
    def __init__(self):
        super().__init__()

        self.title_label = QLabel("Card Preview")
        self.title_label.setStyleSheet("font-size: 22px; font-weight: bold;")

        self.question_label = QLabel("Question")
        self.question_label.setStyleSheet("font-size: 16px; font-weight: bold;")

        self.question_text = QTextEdit()
        self.question_text.setReadOnly(True)

        self.answer_label = QLabel("Answer")
        self.answer_label.setStyleSheet("font-size: 16px; font-weight: bold;")

        self.answer_text = QTextEdit()
        self.answer_text.setReadOnly(True)

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

    def show_card(self, question: str, answer: str):
        self.question_text.setPlainText(question)
        self.answer_text.setPlainText(answer)

    def clear_preview(self):
        self.question_text.setPlainText("")
        self.answer_text.setPlainText("")