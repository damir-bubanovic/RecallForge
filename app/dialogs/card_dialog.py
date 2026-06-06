from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QLabel,
    QTextEdit,
    QVBoxLayout,
)


class CardDialog(QDialog):
    def __init__(
        self,
        parent=None,
        title="Card",
        question_text="",
        answer_text="",
    ):
        super().__init__(parent)

        self.setWindowTitle(title)
        self.setMinimumSize(500, 400)

        self.question_input = QTextEdit()
        self.question_input.setPlainText(question_text)

        self.answer_input = QTextEdit()
        self.answer_input.setPlainText(answer_text)

        self.button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save
            | QDialogButtonBox.StandardButton.Cancel
        )

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Question"))
        layout.addWidget(self.question_input)

        layout.addWidget(QLabel("Answer"))
        layout.addWidget(self.answer_input)

        layout.addWidget(self.button_box)

        self.setLayout(layout)

        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

    def get_data(self):
        return {
            "question_text": self.question_input.toPlainText().strip(),
            "answer_text": self.answer_input.toPlainText().strip(),
        }