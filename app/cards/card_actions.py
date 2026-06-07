from PySide6.QtWidgets import QMessageBox

from app.cards.card_loader import (
    CARD_ANSWER_IMAGE_ROLE,
    CARD_ANSWER_ROLE,
    CARD_ID_ROLE,
    CARD_QUESTION_IMAGE_ROLE,
    CARD_QUESTION_ROLE,
)
from app.dialogs.card_dialog import CardDialog

from database.cards import create_card, delete_card, update_card


def add_card(parent, topic_id: int, reload_callback):
    if topic_id is None:
        QMessageBox.information(parent, "No Topic Selected", "Please select a topic first.")
        return

    dialog = CardDialog(parent=parent, title="Add Card")

    if not dialog.exec():
        return

    data = dialog.get_data()

    try:
        create_card(
            topic_id=topic_id,
            question_text=data["question_text"],
            answer_text=data["answer_text"],
            question_image_path=data["question_image_path"],
            answer_image_path=data["answer_image_path"],
        )
        reload_callback()
    except Exception as error:
        QMessageBox.warning(parent, "Error", str(error))


def edit_card(parent, item, reload_callback):
    card_id = item.data(CARD_ID_ROLE)
    current_question = item.data(CARD_QUESTION_ROLE)
    current_answer = item.data(CARD_ANSWER_ROLE)
    current_question_image = item.data(CARD_QUESTION_IMAGE_ROLE)
    current_answer_image = item.data(CARD_ANSWER_IMAGE_ROLE)

    dialog = CardDialog(
        parent=parent,
        title="Edit Card",
        question_text=current_question,
        answer_text=current_answer,
        question_image_path=current_question_image,
        answer_image_path=current_answer_image,
    )

    if not dialog.exec():
        return

    data = dialog.get_data()

    try:
        update_card(
            card_id=card_id,
            question_text=data["question_text"],
            answer_text=data["answer_text"],
            question_image_path=data["question_image_path"],
            answer_image_path=data["answer_image_path"],
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