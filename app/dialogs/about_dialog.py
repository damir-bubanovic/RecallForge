from PySide6.QtCore import Qt
from PySide6.QtGui import QDesktopServices
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import (
    QDialog,
    QLabel,
    QPushButton,
    QVBoxLayout,
)


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("About RecallForge")
        self.setMinimumWidth(450)

        self.logo = QSvgWidget("assets/logo.svg")
        self.logo.setFixedSize(100, 100)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        layout.addWidget(
            self.logo,
            alignment=Qt.AlignmentFlag.AlignCenter,
        )

        title = QLabel("RecallForge")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(
            "font-size: 22px; font-weight: bold;"
        )

        version = QLabel("Version 0.1")
        version.setAlignment(Qt.AlignmentFlag.AlignCenter)

        description = QLabel(
            "A local-first flashcard learning application "
            "for organizing, reviewing, and retaining knowledge."
        )
        description.setWordWrap(True)
        description.setAlignment(Qt.AlignmentFlag.AlignCenter)

        stack = QLabel(
            "Built with:\n"
            "• Python\n"
            "• PySide6\n"
            "• SQLite"
        )
        stack.setAlignment(Qt.AlignmentFlag.AlignCenter)

        developer = QLabel(
            "Created by:\n"
            "Damir Bubanovic"
        )
        developer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        github = QLabel(
            '<a href="https://github.com/damir-bubanovic/RecallForge">'
            'GitHub Repository'
            '</a>'
        )
        github.setAlignment(Qt.AlignmentFlag.AlignCenter)
        github.setOpenExternalLinks(False)
        github.linkActivated.connect(
            lambda url: QDesktopServices.openUrl(QUrl(url))
        )

        copyright_label = QLabel(
            "© 2026 Damir Bubanovic"
        )
        copyright_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.accept)

        layout.addWidget(title)
        layout.addWidget(version)
        layout.addSpacing(10)

        layout.addWidget(description)
        layout.addSpacing(10)

        layout.addWidget(stack)
        layout.addSpacing(10)

        layout.addWidget(developer)
        layout.addSpacing(10)

        layout.addWidget(github)
        layout.addSpacing(10)

        layout.addWidget(copyright_label)
        layout.addSpacing(20)

        layout.addWidget(close_button)

        self.setLayout(layout)