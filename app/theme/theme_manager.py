LIGHT_THEME = ""

DARK_THEME = """
QWidget {
    background-color: #121212;
    color: #f5f5f5;
}

QLineEdit,
QTextEdit,
QListWidget,
QTreeWidget {
    background-color: #1e1e1e;
    color: #f5f5f5;
    border: 1px solid #444444;
}

QPushButton {
    background-color: #2a2a2a;
    color: #f5f5f5;
    border: 1px solid #555555;
    padding: 6px;
}

QPushButton:hover {
    background-color: #333333;
}

QMenuBar,
QMenu {
    background-color: #1e1e1e;
    color: #f5f5f5;
}
"""


def apply_light_theme(app):
    app.setStyleSheet(LIGHT_THEME)


def apply_dark_theme(app):
    app.setStyleSheet(DARK_THEME)