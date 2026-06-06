from PySide6.QtWidgets import QInputDialog, QMessageBox

from app.cards.card_loader import (
    CARD_ANSWER_ROLE,
    CARD_ID_ROLE,
    CARD_QUESTION_ROLE,
)

from database.cards import create_card, delete_card, update_card


def add_card(parent, topic_id: int, reload_callback):
    if topic_id is None:
        QMessageBox.information(parent, "No Topic Selected", "Please select a topic first.")
        return

    question, ok = QInputDialog.getMultiLineText(
        parent,
        "Add Card",
        "Question:",
    )

    if not ok:
        return

    answer, ok = QInputDialog.getMultiLineText(
        parent,
        "Add Card",
        "Answer:",
    )

    if not ok:
        return

    try:
        create_card(
            topic_id=topic_id,
            question_text=question,
            answer_text=answer,
        )
        reload_callback()
    except Exception as error:
        QMessageBox.warning(parent, "Error", str(error))


def edit_card(parent, item, reload_callback):
    card_id = item.data(CARD_ID_ROLE)
    current_question = item.data(CARD_QUESTION_ROLE)
    current_answer = item.data(CARD_ANSWER_ROLE)

    new_question, ok = QInputDialog.getMultiLineText(
        parent,
        "Edit Card",
        "Question:",
        current_question,
    )

    if not ok:
        return

    new_answer, ok = QInputDialog.getMultiLineText(
        parent,
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
        reload_callback()
    except Exception as error:
        QMessageBox.warning(parent, "Error", str(error))


def remove_card(parent, item, reload_callback):
    card_id = item.data(CARD_ID_ROLE)
    question_text = item.data(CARD_QUESTION_ROLE)

    confirmation = QMessageBox.question(
        parent,
        "Delete Card",
        f"Delete card?\n\n{question_text}",
    )

    if confirmation != QMessageBox.StandardButton.Yes:
        return

    try:
        delete_card(card_id)
        reload_callback()
    except Exception as error:
        QMessageBox.warning(parent, "Error", str(error))