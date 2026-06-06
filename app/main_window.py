from PySide6.QtWidgets import QMainWindow, QLabel
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RecallForge")
        self.setMinimumSize(900, 600)

        welcome_label = QLabel("Welcome to RecallForge")
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(welcome_label)