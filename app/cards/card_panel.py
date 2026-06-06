from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from app.cards.card_actions import add_card
from app.cards.card_loader import load_cards
from app.cards.card_menu import open_context_menu


class CardPanel(QWidget):
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

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(self.title_label)
        layout.addWidget(self.help_label)
        layout.addWidget(self.card_list)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

        self.add_button.clicked.connect(self.handle_add_card)
        self.card_list.customContextMenuRequested.connect(self.show_context_menu)

    def load_cards_for_topic(self, topic_id: int, topic_name: str):
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