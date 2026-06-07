from PySide6.QtWidgets import QHBoxLayout, QMainWindow, QWidget

from app.cards.card_panel import CardPanel
from app.hierarchy.hierarchy_panel import HierarchyPanel
from app.preview.card_preview import CardPreview
from app.search.search_panel import SearchPanel
from app.import_export.exporter import export_to_json
from app.import_export.importer import import_from_json
from app.statistics.statistics_dialog import StatisticsDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RecallForge")
        self.setMinimumSize(1300, 650)

        self.hierarchy_panel = HierarchyPanel()
        self.card_panel = CardPanel()
        self.card_preview = CardPreview()
        self.search_panel = SearchPanel()

        self.setup_ui()
        self.setup_menu()


    def setup_ui(self):
        main_layout = QHBoxLayout()

        main_layout.addWidget(self.hierarchy_panel)
        main_layout.addWidget(self.search_panel)
        main_layout.addWidget(self.card_panel)
        main_layout.addWidget(self.card_preview)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)

        self.hierarchy_panel.topic_selected_signal.connect(self.card_panel.load_cards_for_topic)
        self.card_panel.card_selected_signal.connect(self.card_preview.show_card)
        self.search_panel.topic_selected_signal.connect(self.card_panel.load_cards_for_topic)

    def setup_menu(self):
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("File")

        export_action = file_menu.addAction("Export")
        export_action.triggered.connect(lambda: export_to_json(self))

        import_action = file_menu.addAction("Import")
        import_action.triggered.connect(
            lambda: import_from_json(self, refresh_callback=self.refresh_after_import)
        )

        tools_menu = menu_bar.addMenu("Tools")

        statistics_action = tools_menu.addAction("Statistics")
        statistics_action.triggered.connect(self.open_statistics_dialog)

    def open_statistics_dialog(self):
        dialog = StatisticsDialog(self)
        dialog.exec()

    def refresh_after_import(self):
        self.hierarchy_panel.reload_hierarchy()
        self.card_panel.load_cards_for_topic(None, "")
        self.card_preview.clear_preview()
