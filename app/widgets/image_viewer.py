from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import QLabel, QSizePolicy, QVBoxLayout, QWidget


class ImageViewer(QWidget):
    def __init__(self, width: int = 300, height: int = 180):
        super().__init__()

        self.viewer_width = width
        self.viewer_height = height

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.svg_widget = QSvgWidget()
        self.svg_widget.setFixedSize(self.viewer_width, self.viewer_height)
        self.svg_widget.setSizePolicy(
            QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Fixed,
        )

        self.setup_ui()
        self.clear()

    def setup_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(self.image_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.svg_widget, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def show_image(self, image_path: str | None):
        self.clear()

        if not image_path:
            return

        path = Path(image_path)

        if not path.exists():
            return

        if path.suffix.lower() == ".svg":
            self.svg_widget.load(str(path))
            self.svg_widget.show()
            return

        pixmap = QPixmap(str(path))

        if pixmap.isNull():
            return

        scaled_pixmap = pixmap.scaled(
            self.viewer_width,
            self.viewer_height,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )

        self.image_label.setPixmap(scaled_pixmap)
        self.image_label.show()

    def clear(self):
        self.image_label.clear()
        self.image_label.hide()
        self.svg_widget.hide()