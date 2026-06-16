from PySide6.QtCore import Qt, Signal
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import QLabel, QHBoxLayout, QTreeWidget, QVBoxLayout, QWidget
from app.styles.font_sizes import FONT_SIZE_APP_TITLE, font_size_px

from app.hierarchy.hierarchy_loader import (
    ITEM_ID_ROLE,
    ITEM_TYPE_ROLE,
    load_hierarchy,
)
from app.hierarchy.hierarchy_menu import open_context_menu
from app.utils.paths import get_asset_path


class HierarchyPanel(QWidget):
    topic_selected_signal = Signal(int, str)

    def __init__(self):
        super().__init__()

        self.logo = QSvgWidget(get_asset_path("logo.svg"))
        self.logo.setFixedSize(40, 40)

        self.app_title_label = QLabel("RecallForge")
        self.app_title_label.setStyleSheet(
            f"{font_size_px(FONT_SIZE_APP_TITLE)} font-weight: bold;"
        )

        self.tree = QTreeWidget()
        self.tree.setHeaderLabel("Subjects / Topics")
        self.tree.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        self.setup_ui()
        self.reload_hierarchy()

    def setup_ui(self):
        layout = QVBoxLayout()

        header_layout = QHBoxLayout()
        header_layout.addWidget(self.logo)
        header_layout.addWidget(self.app_title_label)
        header_layout.addStretch()

        layout.addLayout(header_layout)
        layout.addWidget(self.tree)

        self.setLayout(layout)
        self.setFixedWidth(300)

        self.tree.customContextMenuRequested.connect(self.show_context_menu)
        self.tree.itemClicked.connect(self.handle_item_clicked)

    def reload_hierarchy(self):
        load_hierarchy(self.tree)

    def show_context_menu(self, position):
        open_context_menu(
            parent=self,
            tree=self.tree,
            position=position,
            reload_callback=self.reload_hierarchy,
        )

    def handle_item_clicked(self, item):
        item_type = item.data(0, ITEM_TYPE_ROLE)

        if item_type != "topic":
            return

        topic_id = item.data(0, ITEM_ID_ROLE)
        topic_name = item.text(0)

        self.topic_selected_signal.emit(topic_id, topic_name)