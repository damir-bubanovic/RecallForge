from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import QLabel, QSizePolicy, QTextEdit, QVBoxLayout, QWidget


class CardPreview(QWidget):
    def __init__(self):
        super().__init__()

        self.title_label = QLabel("Card Preview")
        self.title_label.setStyleSheet("font-size: 22px; font-weight: bold;")

        self.question_label = QLabel("Question")
        self.question_label.setStyleSheet("font-size: 16px; font-weight: bold;")

        self.question_text = QTextEdit()
        self.question_text.setReadOnly(True)

        self.question_image_label = QLabel()
        self.question_image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.question_svg_widget = QSvgWidget()
        self.question_svg_widget.setFixedSize(300, 180)
        self.question_svg_widget.setSizePolicy(
            QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Fixed,
        )

        self.answer_label = QLabel("Answer")
        self.answer_label.setStyleSheet("font-size: 16px; font-weight: bold;")

        self.answer_text = QTextEdit()
        self.answer_text.setReadOnly(True)

        self.answer_image_label = QLabel()
        self.answer_image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.answer_svg_widget = QSvgWidget()
        self.answer_svg_widget.setFixedSize(300, 180)
        self.answer_svg_widget.setSizePolicy(
            QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Fixed,
        )

        self.setup_ui()
        self.clear_preview()

    def setup_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(self.title_label)

        layout.addWidget(self.question_label)
        layout.addWidget(self.question_text)
        layout.addWidget(self.question_image_label)
        layout.addWidget(self.question_svg_widget)

        layout.addWidget(self.answer_label)
        layout.addWidget(self.answer_text)
        layout.addWidget(self.answer_image_label)
        layout.addWidget(self.answer_svg_widget)

        self.setLayout(layout)

    def show_card(
        self,
        question: str,
        answer: str,
        question_image_path: str | None = None,
        answer_image_path: str | None = None,
    ):
        self.question_text.setPlainText(question)
        self.answer_text.setPlainText(answer)

        self.display_image(
            image_path=question_image_path,
            image_label=self.question_image_label,
            svg_widget=self.question_svg_widget,
        )

        self.display_image(
            image_path=answer_image_path,
            image_label=self.answer_image_label,
            svg_widget=self.answer_svg_widget,
        )

    @staticmethod
    def display_image(image_path, image_label, svg_widget):
        image_label.clear()
        image_label.hide()
        svg_widget.hide()

        if not image_path:
            return

        path = Path(image_path)

        if not path.exists():
            return

        if path.suffix.lower() == ".svg":
            svg_widget.load(str(path))
            svg_widget.show()
            return

        pixmap = QPixmap(str(path))

        if pixmap.isNull():
            return

        scaled_pixmap = pixmap.scaled(
            300,
            180,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )

        image_label.setPixmap(scaled_pixmap)
        image_label.show()

    def clear_preview(self):
        self.question_text.setPlainText("")
        self.answer_text.setPlainText("")

        self.question_image_label.clear()
        self.answer_image_label.clear()

        self.question_image_label.hide()
        self.answer_image_label.hide()

        self.question_svg_widget.hide()
        self.answer_svg_widget.hide()