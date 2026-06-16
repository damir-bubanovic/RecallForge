from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidgetItem
from PySide6.QtGui import QTextDocument

from database.cards import get_cards_by_topic


CARD_ID_ROLE = Qt.ItemDataRole.UserRole
CARD_QUESTION_ROLE = Qt.ItemDataRole.UserRole + 1
CARD_ANSWER_ROLE = Qt.ItemDataRole.UserRole + 2
CARD_QUESTION_IMAGE_ROLE = Qt.ItemDataRole.UserRole + 3
CARD_ANSWER_IMAGE_ROLE = Qt.ItemDataRole.UserRole + 4


def html_to_plain_text(content: str) -> str:
    document = QTextDocument()
    document.setHtml(content or "")
    return document.toPlainText().strip()

def load_cards(card_list, topic_id: int):
    card_list.clear()

    cards = get_cards_by_topic(topic_id)

    for card in cards:
        item = QListWidgetItem(html_to_plain_text(card["question_text"]))
        item.setData(CARD_ID_ROLE, card["id"])
        item.setData(CARD_QUESTION_ROLE, card["question_text"])
        item.setData(CARD_ANSWER_ROLE, card["answer_text"])
        item.setData(CARD_QUESTION_IMAGE_ROLE, card["question_image_path"])
        item.setData(CARD_ANSWER_IMAGE_ROLE, card["answer_image_path"])

        card_list.addItem(item)