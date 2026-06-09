import sys

from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QApplication

from app.main_window import MainWindow
from app.theme.theme_manager import apply_dark_theme, apply_light_theme
from database.schema import initialize_database


def main():
    initialize_database()

    app = QApplication(sys.argv)

    settings = QSettings("RecallForge", "RecallForge")
    dark_mode_enabled = settings.value("dark_mode_enabled", False, type=bool)

    if dark_mode_enabled:
        apply_dark_theme(app)
    else:
        apply_light_theme(app)

    window = MainWindow(dark_mode_enabled=dark_mode_enabled)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()