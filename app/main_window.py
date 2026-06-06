from PySide6.QtWidgets import QHBoxLayout, QLabel, QMainWindow, QVBoxLayout, QWidget

from app.hierarchy_panel import HierarchyPanel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RecallForge")
        self.setMinimumSize(1000, 600)

        self.hierarchy_panel = HierarchyPanel()

        self.placeholder_label = QLabel(
            "Right-click the hierarchy to add subjects and topics.\nSelect a topic to manage cards."
        )
        self.placeholder_label.setStyleSheet("font-size: 22px;")

        self.setup_ui()

    def setup_ui(self):
        main_layout = QHBoxLayout()

        content_layout = QVBoxLayout()
        content_layout.addWidget(self.placeholder_label)

        content_widget = QWidget()
        content_widget.setLayout(content_layout)

        main_layout.addWidget(self.hierarchy_panel)
        main_layout.addWidget(content_widget)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)

        self.hierarchy_panel.topic_selected_signal.connect(self.topic_selected)

    def topic_selected(self, _topic_id: int, topic_name: str):
        self.placeholder_label.setText(f"Selected topic: {topic_name}")