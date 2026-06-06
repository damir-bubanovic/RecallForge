import sys

from PySide6.QtWidgets import QApplication

from app.main_window import MainWindow
from database.db import initialize_database, create_subject, get_subjects


def main():
    initialize_database()

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()