from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidgetItem

from database.cards import get_cards_by_topic


CARD_ID_ROLE = Qt.ItemDataRole.UserRole
CARD_QUESTION_ROLE = Qt.ItemDataRole.UserRole + 1
CARD_ANSWER_ROLE = Qt.ItemDataRole.UserRole + 2


def load_cards(card_list, topic_id: int):
    card_list.clear()

    cards = get_cards_by_topic(topic_id)

    for card in cards:
        item = QListWidgetItem(card["question_text"])
        item.setData(CARD_ID_ROLE, card["id"])
        item.setData(CARD_QUESTION_ROLE, card["question_text"])
        item.setData(CARD_ANSWER_ROLE, card["answer_text"])

        card_list.addItem(item)