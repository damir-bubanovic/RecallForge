from PySide6.QtWidgets import QMainWindow

from app.subject_panel import SubjectPanel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RecallForge")
        self.setMinimumSize(900, 600)

        self.subject_panel = SubjectPanel()
        self.setCentralWidget(self.subject_panel)