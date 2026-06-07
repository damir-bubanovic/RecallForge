from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog,
    QLabel,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
)

from database.cards import get_cards_by_topic


class ReviewDialog(QDialog):
    def __init__(self, parent=None, topic_id=None, topic_name=""):
        super().__init__(parent)

        self.topic_id = topic_id
        self.topic_name = topic_name
        self.cards = get_cards_by_topic(topic_id)

        self.current_index = 0
        self.showing_answer = False

        self.setWindowTitle(f"Review: {topic_name}")
        self.setMinimumSize(700, 500)

        self.progress_label = QLabel()
        self.progress_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.card_text_label = QLabel()
        self.card_text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.card_text_label.setWordWrap(True)
        self.card_text_label.setStyleSheet("font-size: 26px;")

        self.click_button = QPushButton("Show Answer")
        self.click_button.setMinimumHeight(50)

        self.setup_ui()
        self.load_current_question()

    def setup_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(self.progress_label)
        layout.addWidget(self.card_text_label)
        layout.addWidget(self.click_button)

        self.setLayout(layout)

        self.click_button.clicked.connect(self.handle_click)

    def load_current_question(self):
        if not self.cards:
            QMessageBox.information(
                self,
                "No Cards",
                "This topic has no cards to review.",
            )
            self.close()
            return

        card = self.cards[self.current_index]

        self.showing_answer = False
        self.progress_label.setText(
            f"Card {self.current_index + 1} of {len(self.cards)}"
        )
        self.card_text_label.setText(card["question_text"])
        self.click_button.setText("Show Answer")

    def show_answer(self):
        card = self.cards[self.current_index]

        self.showing_answer = True
        self.card_text_label.setText(card["answer_text"])
        self.click_button.setText("Next Question")

    def move_to_next_card(self):
        self.current_index += 1

        if self.current_index >= len(self.cards):
            QMessageBox.information(
                self,
                "Review Complete",
                "You reviewed all cards in this topic.",
            )
            self.current_index = 0

        self.load_current_question()

    def handle_click(self):
        if not self.showing_answer:
            self.show_answer()
        else:
            self.move_to_next_card()