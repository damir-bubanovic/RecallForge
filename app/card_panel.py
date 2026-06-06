from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QInputDialog,
    QListWidget,
    QListWidgetItem,
    QMenu,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
)

from database.cards import (
    create_card,
    delete_card,
    get_cards_by_topic,
    update_card,
)


CARD_ID_ROLE = Qt.ItemDataRole.UserRole


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

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        add_button = QPushButton("Add Card")
        add_button.clicked.connect(self.add_card)

        layout.addWidget(self.title_label)
        layout.addWidget(self.help_label)
        layout.addWidget(self.card_list)
        layout.addWidget(add_button)

        self.setLayout(layout)

        self.card_list.customContextMenuRequested.connect(self.open_context_menu)

    def load_cards(self, topic_id: int, topic_name: str):
        self.current_topic_id = topic_id
        self.current_topic_name = topic_name

        self.title_label.setText(f"Cards: {topic_name}")
        self.help_label.setText("Right-click a card to edit or delete it.")

        self.card_list.clear()

        cards = get_cards_by_topic(topic_id)

        for card in cards:
            item = QListWidgetItem(card["question_text"])
            item.setData(CARD_ID_ROLE, card["id"])
            item.setData(CARD_ID_ROLE + 1, card["question_text"])
            item.setData(CARD_ID_ROLE + 2, card["answer_text"])
            self.card_list.addItem(item)

    def add_card(self):
        if self.current_topic_id is None:
            QMessageBox.information(self, "No Topic Selected", "Please select a topic first.")
            return

        question, ok = QInputDialog.getMultiLineText(
            self,
            "Add Card",
            "Question:",
        )

        if not ok:
            return

        answer, ok = QInputDialog.getMultiLineText(
            self,
            "Add Card",
            "Answer:",
        )

        if not ok:
            return

        try:
            create_card(
                topic_id=self.current_topic_id,
                question_text=question,
                answer_text=answer,
            )
            self.load_cards(self.current_topic_id, self.current_topic_name)
        except Exception as error:
            QMessageBox.warning(self, "Error", str(error))

    def open_context_menu(self, position):
        item = self.card_list.itemAt(position)

        if item is None:
            menu = QMenu(self)
            add_card_action = menu.addAction("Add Card")

            selected_action = menu.exec(self.card_list.viewport().mapToGlobal(position))

            if selected_action == add_card_action:
                self.add_card()

            return

        menu = QMenu(self)
        edit_card_action = menu.addAction("Edit Card")
        delete_card_action = menu.addAction("Delete Card")

        selected_action = menu.exec(self.card_list.viewport().mapToGlobal(position))

        if selected_action == edit_card_action:
            self.edit_card(item)
        elif selected_action == delete_card_action:
            self.remove_card(item)

    def edit_card(self, item):
        card_id = item.data(CARD_ID_ROLE)
        current_question = item.data(CARD_ID_ROLE + 1)
        current_answer = item.data(CARD_ID_ROLE + 2)

        new_question, ok = QInputDialog.getMultiLineText(
            self,
            "Edit Card",
            "Question:",
            current_question,
        )

        if not ok:
            return

        new_answer, ok = QInputDialog.getMultiLineText(
            self,
            "Edit Card",
            "Answer:",
            current_answer,
        )

        if not ok:
            return

        try:
            update_card(
                card_id=card_id,
                question_text=new_question,
                answer_text=new_answer,
            )
            self.load_cards(self.current_topic_id, self.current_topic_name)
        except Exception as error:
            QMessageBox.warning(self, "Error", str(error))

    def remove_card(self, item):
        card_id = item.data(CARD_ID_ROLE)
        question_text = item.data(CARD_ID_ROLE + 1)

        confirmation = QMessageBox.question(
            self,
            "Delete Card",
            f"Delete card?\n\n{question_text}",
        )

        if confirmation != QMessageBox.StandardButton.Yes:
            return

        try:
            delete_card(card_id)
            self.load_cards(self.current_topic_id, self.current_topic_name)
        except Exception as error:
            QMessageBox.warning(self, "Error", str(error))