from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QSizePolicy,
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
        self.setMinimumSize(800, 650)

        self.progress_label = QLabel()
        self.progress_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.card_text_label = QLabel()
        self.card_text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.card_text_label.setWordWrap(True)
        self.card_text_label.setStyleSheet("font-size: 26px;")

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.svg_widget = QSvgWidget()
        self.svg_widget.setFixedSize(420, 260)
        self.svg_widget.setSizePolicy(
            QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Fixed,
        )

        self.show_answer_button = QPushButton("Show Answer")
        self.show_answer_button.setMinimumHeight(50)

        self.again_button = QPushButton("Again")
        self.hard_button = QPushButton("Hard")
        self.good_button = QPushButton("Good")
        self.easy_button = QPushButton("Easy")

        self.setup_ui()
        self.load_current_question()

    def setup_ui(self):
        layout = QVBoxLayout()

        rating_layout = QHBoxLayout()
        rating_layout.addWidget(self.again_button)
        rating_layout.addWidget(self.hard_button)
        rating_layout.addWidget(self.good_button)
        rating_layout.addWidget(self.easy_button)

        layout.addWidget(self.progress_label)
        layout.addWidget(self.card_text_label)
        layout.addWidget(self.image_label)
        layout.addWidget(self.svg_widget)
        layout.addWidget(self.show_answer_button)
        layout.addLayout(rating_layout)

        self.setLayout(layout)

        self.show_answer_button.clicked.connect(self.show_answer)

        self.again_button.clicked.connect(self.rate_again)
        self.hard_button.clicked.connect(self.rate_hard)
        self.good_button.clicked.connect(self.rate_good)
        self.easy_button.clicked.connect(self.rate_easy)

    def set_rating_buttons_visible(self, visible: bool):
        self.again_button.setVisible(visible)
        self.hard_button.setVisible(visible)
        self.good_button.setVisible(visible)
        self.easy_button.setVisible(visible)

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

        self.display_image(card["question_image_path"])

        self.show_answer_button.setVisible(True)
        self.set_rating_buttons_visible(False)

    def show_answer(self):
        card = self.cards[self.current_index]

        self.showing_answer = True
        self.card_text_label.setText(card["answer_text"])

        self.display_image(card["answer_image_path"])

        self.show_answer_button.setVisible(False)
        self.set_rating_buttons_visible(True)

    def display_image(self, image_path):
        self.image_label.clear()
        self.image_label.hide()
        self.svg_widget.hide()

        if not image_path:
            return

        path = Path(image_path)

        if not path.exists():
            return

        if path.suffix.lower() == ".svg":
            self.svg_widget.load(str(path))
            self.svg_widget.show()
            return

        pixmap = QPixmap(str(path))

        if pixmap.isNull():
            return

        scaled_pixmap = pixmap.scaled(
            420,
            260,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )

        self.image_label.setPixmap(scaled_pixmap)
        self.image_label.show()

    def move_to_next_card(self):
        self.current_index += 1

        if self.current_index >= len(self.cards):
            QMessageBox.information(
                self,
                "Review Complete",
                "You reviewed all cards in this topic.",
            )
            self.accept()
            return

        self.load_current_question()

    def rate_again(self):
        current_card = self.cards[self.current_index]
        self.cards.append(current_card)
        self.move_to_next_card()

    def rate_hard(self):
        self.move_to_next_card()

    def rate_good(self):
        self.move_to_next_card()

    def rate_easy(self):
        self.move_to_next_card()