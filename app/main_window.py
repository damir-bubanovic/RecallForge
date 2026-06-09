from PySide6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QWidget
from PySide6.QtCore import QSettings
from PySide6.QtGui import QIcon

from app.cards.card_panel import CardPanel
from app.hierarchy.hierarchy_panel import HierarchyPanel
from app.import_export.exporter import export_to_json
from app.import_export.importer import import_from_json
from app.preview.card_preview import CardPreview
from app.search.search_panel import SearchPanel
from app.dialogs.about_dialog import AboutDialog
from app.statistics.statistics_dialog import StatisticsDialog
from app.theme.theme_manager import apply_dark_theme, apply_light_theme


class MainWindow(QMainWindow):
    def __init__(self, dark_mode_enabled=False):
        super().__init__()

        self.setWindowTitle("RecallForge")
        self.setWindowIcon(QIcon("assets/logo.svg"))
        self.setMinimumSize(1300, 650)

        self.dark_mode_enabled = dark_mode_enabled
        self.dark_mode_action = None

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

        self.hierarchy_panel.topic_selected_signal.connect(
            self.card_panel.load_cards_for_topic
        )
        self.card_panel.card_selected_signal.connect(
            self.card_preview.show_card
        )
        self.search_panel.topic_selected_signal.connect(
            self.card_panel.load_cards_for_topic
        )

    def setup_menu(self):
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("File")

        export_action = file_menu.addAction("Export")
        export_action.triggered.connect(lambda: export_to_json(self))

        import_action = file_menu.addAction("Import")
        import_action.triggered.connect(
            lambda: import_from_json(
                self,
                refresh_callback=self.refresh_after_import,
            )
        )

        tools_menu = menu_bar.addMenu("Tools")

        statistics_action = tools_menu.addAction("Statistics")
        statistics_action.triggered.connect(self.open_statistics_dialog)

        view_menu = menu_bar.addMenu("View")

        self.dark_mode_action = view_menu.addAction("Dark Mode")
        self.dark_mode_action.setCheckable(True)
        self.dark_mode_action.setChecked(self.dark_mode_enabled)
        self.dark_mode_action.triggered.connect(self.toggle_dark_mode)

        help_menu = menu_bar.addMenu("Help")

        about_action = help_menu.addAction("About")
        about_action.triggered.connect(self.open_about_dialog)

    def open_statistics_dialog(self):
        dialog = StatisticsDialog(self)
        dialog.exec()

    def open_about_dialog(self):
        dialog = AboutDialog(self)
        dialog.exec()

    def toggle_dark_mode(self):
        app = QApplication.instance()
        settings = QSettings("RecallForge", "RecallForge")

        if self.dark_mode_action.isChecked():
            apply_dark_theme(app)
            self.dark_mode_enabled = True
        else:
            apply_light_theme(app)
            self.dark_mode_enabled = False

        settings.setValue("dark_mode_enabled", self.dark_mode_enabled)

    def refresh_after_import(self):
        self.hierarchy_panel.reload_hierarchy()
        self.card_panel.load_cards_for_topic(None, "")
        self.card_preview.clear_preview()