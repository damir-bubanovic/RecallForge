from PySide6.QtWidgets import QMenu

from app.cards.card_actions import add_card, edit_card, remove_card


def open_context_menu(parent, card_list, position, topic_id, reload_callback):
    item = card_list.itemAt(position)

    menu = QMenu(parent)

    if item is None:
        add_card_action = menu.addAction("Add Card")

        selected_action = menu.exec(card_list.viewport().mapToGlobal(position))

        if selected_action == add_card_action:
            add_card(parent, topic_id, reload_callback)

        return

    edit_card_action = menu.addAction("Edit Card")
    delete_card_action = menu.addAction("Delete Card")

    selected_action = menu.exec(card_list.viewport().mapToGlobal(position))

    if selected_action == edit_card_action:
        edit_card(parent, item, reload_callback)
    elif selected_action == delete_card_action:
        remove_card(parent, item, reload_callback)