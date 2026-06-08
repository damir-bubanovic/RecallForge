from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QLabel,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from app.cards.card_actions import add_card
from app.cards.card_loader import (
    CARD_ANSWER_IMAGE_ROLE,
    CARD_ANSWER_ROLE,
    CARD_QUESTION_IMAGE_ROLE,
    CARD_QUESTION_ROLE,
    load_cards,
)
from app.cards.card_menu import open_context_menu
from app.review.review_dialog import ReviewDialog



class CardPanel(QWidget):
    card_selected_signal = Signal(str, str, object, object)

    def __init__(self):
        super().__init__()

        self.current_topic_id = None
        self.current_topic_name = None

        self.title_label = QLabel("Cards")
        self.title_label.setStyleSheet("font-size: 22px; font-weight: bold;")

        self.help_label = QLabel("Select a topic to manage cards.")

        self.card_list = QListWidget()
        self.card_list.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        self.add_button = QPushButton("Add Card")
        self.review_button = QPushButton("Start Review")

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(self.title_label)
        layout.addWidget(self.help_label)
        layout.addWidget(self.card_list)
        layout.addWidget(self.add_button)
        layout.addWidget(self.review_button)

        self.setLayout(layout)

        self.add_button.clicked.connect(self.handle_add_card)
        self.review_button.clicked.connect(self.start_review)
        self.card_list.customContextMenuRequested.connect(self.show_context_menu)
        self.card_list.itemClicked.connect(self.handle_card_selected)

    def clear_topic_selection(self):
        self.current_topic_id = None
        self.current_topic_name = None
        self.title_label.setText("Cards")
        self.help_label.setText("Select a topic to manage cards.")
        self.card_list.clear()

    def load_cards_for_topic(self, topic_id: int | None, topic_name: str):
        if topic_id is None:
            self.clear_topic_selection()
            return

        self.current_topic_id = topic_id
        self.current_topic_name = topic_name

        self.title_label.setText(f"Cards: {topic_name}")
        self.help_label.setText("Right-click a card to edit or delete it.")

        load_cards(self.card_list, topic_id)

    def reload_cards(self):
        if self.current_topic_id is None:
            return

        load_cards(self.card_list, self.current_topic_id)

    def handle_add_card(self):
        add_card(
            parent=self,
            topic_id=self.current_topic_id,
            reload_callback=self.reload_cards,
        )

    def show_context_menu(self, position):
        open_context_menu(
            parent=self,
            card_list=self.card_list,
            position=position,
            topic_id=self.current_topic_id,
            reload_callback=self.reload_cards,
        )

    def handle_card_selected(self, item):
        question = item.data(CARD_QUESTION_ROLE)
        answer = item.data(CARD_ANSWER_ROLE)
        question_image_path = item.data(CARD_QUESTION_IMAGE_ROLE)
        answer_image_path = item.data(CARD_ANSWER_IMAGE_ROLE)

        self.card_selected_signal.emit(
            question,
            answer,
            question_image_path,
            answer_image_path,
        )

    def start_review(self):
        if self.current_topic_id is None:
            return

        dialog = ReviewDialog(
            parent=self,
            topic_id=self.current_topic_id,
            topic_name=self.current_topic_name,
        )
        dialog.exec()