from PySide6.QtWidgets import QHBoxLayout, QMainWindow, QWidget

from app.cards.card_panel import CardPanel
from app.hierarchy.hierarchy_panel import HierarchyPanel
from app.preview.card_preview import CardPreview


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RecallForge")
        self.setMinimumSize(1300, 650)

        self.hierarchy_panel = HierarchyPanel()
        self.card_panel = CardPanel()
        self.card_preview = CardPreview()

        self.setup_ui()

    def setup_ui(self):
        main_layout = QHBoxLayout()

        main_layout.addWidget(self.hierarchy_panel)
        main_layout.addWidget(self.card_panel)
        main_layout.addWidget(self.card_preview)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)

        self.hierarchy_panel.topic_selected_signal.connect(self.card_panel.load_cards_for_topic)
        self.card_panel.card_selected_signal.connect(self.card_preview.show_card)