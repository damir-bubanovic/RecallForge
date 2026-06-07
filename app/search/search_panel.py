from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QVBoxLayout,
    QWidget,
)

from database.search import search_all


RESULT_TYPE_ROLE = Qt.ItemDataRole.UserRole
RESULT_ID_ROLE = Qt.ItemDataRole.UserRole + 1
RESULT_TOPIC_ID_ROLE = Qt.ItemDataRole.UserRole + 2


class SearchPanel(QWidget):
    topic_selected_signal = Signal(int, str)

    def __init__(self):
        super().__init__()

        self.title_label = QLabel("Search")
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold;")

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
            result_type = result["result_type"]
            title = result["title"]
            subtitle = result["subtitle"]
            topic_id = result["topic_id"]

            display_text = self.format_result_text(result_type, title, subtitle)

            item = QListWidgetItem(display_text)
            item.setData(RESULT_TYPE_ROLE, result_type)
            item.setData(RESULT_ID_ROLE, result["result_id"])
            item.setData(RESULT_TOPIC_ID_ROLE, topic_id)

            self.results_list.addItem(item)

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