from PySide6.QtWidgets import QHBoxLayout, QMainWindow, QWidget

from app.card_panel import CardPanel
from app.hierarchy.hierarchy_panel import HierarchyPanel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RecallForge")
        self.setMinimumSize(1100, 600)

        self.hierarchy_panel = HierarchyPanel()
        self.card_panel = CardPanel()

        self.setup_ui()

    def setup_ui(self):
        main_layout = QHBoxLayout()

        main_layout.addWidget(self.hierarchy_panel)
        main_layout.addWidget(self.card_panel)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)

        self.hierarchy_panel.topic_selected_signal.connect(self.card_panel.load_cards)