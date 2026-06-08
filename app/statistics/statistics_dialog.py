from PySide6.QtWidgets import (
    QDialog,
    QLabel,
    QPushButton,
    QVBoxLayout,
)

from database.statistics import get_basic_statistics


class StatisticsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Statistics")
        self.setMinimumWidth(350)

        stats = get_basic_statistics()

        layout = QVBoxLayout()

        layout.addWidget(
            QLabel(f"Total Subjects: {stats['total_subjects']}")
        )

        layout.addWidget(
            QLabel(f"Total Topics: {stats['total_topics']}")
        )

        layout.addWidget(
            QLabel(f"Total Cards: {stats['total_cards']}")
        )

        layout.addWidget(
            QLabel(
                f"Cards With Images: {stats['total_cards_with_images']}"
            )
        )

        layout.addWidget(
            QLabel(f"Cards Without Images: {stats['total_cards_without_images']}")
        )

        layout.addWidget(
            QLabel(f"Average Cards Per Topic: {stats['average_cards_per_topic']}")
        )

        layout.addWidget(
            QLabel(f"Largest Topic Card Count: {stats['largest_topic_card_count']}")
        )

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.accept)

        layout.addWidget(close_button)

        self.setLayout(layout)