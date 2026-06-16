from PySide6.QtCore import Qt
from PySide6.QtGui import QTextDocument
from PySide6.QtWidgets import QListWidgetItem

from database.cards import get_cards_by_topic


CARD_ID_ROLE = Qt.ItemDataRole.UserRole
CARD_QUESTION_ROLE = Qt.ItemDataRole.UserRole + 1
CARD_ANSWER_ROLE = Qt.ItemDataRole.UserRole + 2


def html_to_plain_text(content: str | None) -> str:
    document = QTextDocument()
    document.setHtml(content or "")
    return document.toPlainText().strip()


def card_list_title(content: str | None) -> str:
    plain_text = html_to_plain_text(content)
    lines = [line.strip() for line in plain_text.splitlines() if line.strip()]

    if not lines:
        return "Untitled Card"

    return lines[0]


def load_cards(card_list, topic_id: int):
    card_list.clear()

    cards = get_cards_by_topic(topic_id)

    for card in cards:
        item = QListWidgetItem(card_list_title(card["question_text"]))
        item.setData(CARD_ID_ROLE, card["id"])
        item.setData(CARD_QUESTION_ROLE, card["question_text"])
        item.setData(CARD_ANSWER_ROLE, card["answer_text"])

        card_list.addItem(item)