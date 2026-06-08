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
        self.setMinimumWidth(450)

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

        layout.addSpacing(10)

        topics_label = QLabel("Top Topics")
        topics_label.setStyleSheet("font-weight: bold;")
        layout.addWidget(topics_label)

        for topic in stats["top_topics"]:
            layout.addWidget(
                QLabel(
                    f"{topic['topic_name']} ({topic['card_count']} cards)"
                )
            )

        layout.addSpacing(10)

        subjects_label = QLabel("Top Subjects")
        subjects_label.setStyleSheet("font-weight: bold;")
        layout.addWidget(subjects_label)

        for subject in stats["top_subjects"]:
            layout.addWidget(
                QLabel(
                    f"{subject['subject_name']} ({subject['card_count']} cards)"
                )
            )

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.accept)

        layout.addWidget(close_button)

        self.setLayout(layout)