from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QTextDocument
from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QVBoxLayout,
    QWidget,
)

from database.search import search_all
from app.styles.font_sizes import FONT_SIZE_SECTION_TITLE, font_size_px


RESULT_TYPE_ROLE = Qt.ItemDataRole.UserRole
RESULT_ID_ROLE = Qt.ItemDataRole.UserRole + 1
RESULT_TOPIC_ID_ROLE = Qt.ItemDataRole.UserRole + 2


def html_to_plain_text(content: str | None) -> str:
    document = QTextDocument()
    document.setHtml(content or "")
    return document.toPlainText().strip()


class SearchPanel(QWidget):
    topic_selected_signal = Signal(int, str)

    def __init__(self):
        super().__init__()

        self.title_label = QLabel("Search")
        self.title_label.setStyleSheet(
            f"{font_size_px(FONT_SIZE_SECTION_TITLE)} font-weight: bold;"
        )

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search subjects, topics, cards...")

        self.results_list = QListWidget()

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(self.title_label)
        layout.addWidget(self.search_input)
        layout.addWidget(self.results_list)

        self.setLayout(layout)
        self.setFixedWidth(320)

        self.search_input.textChanged.connect(self.handle_search)
        self.results_list.itemClicked.connect(self.handle_result_clicked)

    def handle_search(self, text: str):
        self.results_list.clear()

        results = search_all(text)

        for result in results:
            item = self.create_result_item(result)
            self.results_list.addItem(item)

    def create_result_item(self, result):
        result_type = result["result_type"]
        title = html_to_plain_text(result["title"])
        subtitle = html_to_plain_text(result["subtitle"])
        topic_id = result["topic_id"]

        display_text = self.format_result_text(result_type, title, subtitle)

        item = QListWidgetItem(display_text)
        item.setData(RESULT_TYPE_ROLE, result_type)
        item.setData(RESULT_ID_ROLE, result["result_id"])
        item.setData(RESULT_TOPIC_ID_ROLE, topic_id)

        return item

    @staticmethod
    def format_result_text(result_type: str, title: str, subtitle: str | None):
        label = result_type.upper()

        if subtitle:
            return f"[{label}] {title}\n{subtitle}"

        return f"[{label}] {title}"

    def handle_result_clicked(self, item):
        result_type = item.data(RESULT_TYPE_ROLE)

        if result_type == "subject":
            return

        topic_id = item.data(RESULT_TOPIC_ID_ROLE)

        if topic_id is None:
            return

        title = item.text().split("\n")[0]

        self.topic_selected_signal.emit(topic_id, title)