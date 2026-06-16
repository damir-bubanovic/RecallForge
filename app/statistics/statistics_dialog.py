from PySide6.QtWidgets import (
    QDialog,
    QPushButton,
    QScrollArea,
    QWidget,
    QVBoxLayout,
)

from app.statistics.statistics_section import StatisticsSection
from database.statistics import get_basic_statistics


class StatisticsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Statistics")
        self.setMinimumWidth(450)

        stats = get_basic_statistics()

        content_widget = QWidget()
        layout = QVBoxLayout()
        content_widget.setLayout(layout)

        collection_section = StatisticsSection(
            "Collection Statistics",
            [
                ("Total Subjects", stats["total_subjects"]),
                ("Total Topics", stats["total_topics"]),
                ("Total Cards", stats["total_cards"]),
                ("Average Cards Per Topic", stats["average_cards_per_topic"]),
                ("Largest Topic Card Count", stats["largest_topic_card_count"]),
            ],
        )

        layout.addWidget(collection_section)

        top_topics_rows = []

        for topic in stats["top_topics"]:
            top_topics_rows.append(
                (
                    topic["topic_name"],
                    f"{topic['card_count']} cards",
                )
            )

        top_topics_section = StatisticsSection(
            "Top Topics",
            top_topics_rows,
        )

        layout.addWidget(top_topics_section)

        top_subjects_rows = []

        for subject in stats["top_subjects"]:
            top_subjects_rows.append(
                (
                    subject["subject_name"],
                    f"{subject['card_count']} cards",
                )
            )

        top_subjects_section = StatisticsSection(
            "Top Subjects",
            top_subjects_rows,
        )

        layout.addWidget(top_subjects_section)

        review_section = StatisticsSection(
            "Review Statistics",
            [
                ("Total Reviews", stats["total_reviews"]),
                ("Reviews Today", stats["reviews_today"]),
                ("Reviews This Week", stats["reviews_this_week"]),
                ("Again Reviews", stats["again_reviews"]),
                ("Hard Reviews", stats["hard_reviews"]),
                ("Good Reviews", stats["good_reviews"]),
                ("Easy Reviews", stats["easy_reviews"]),
            ],
        )

        layout.addWidget(review_section)

        learning_section = StatisticsSection(
            "Learning Statistics",
            [
                ("New Cards", stats["learning_strengths"]["New"]),
                ("Weak Cards", stats["learning_strengths"]["Weak"]),
                ("Familiar Cards", stats["learning_strengths"]["Familiar"]),
                ("Strong Cards", stats["learning_strengths"]["Strong"]),
            ],
        )

        layout.addWidget(learning_section)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(content_widget)
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.accept)

        layout.addWidget(close_button)

        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(scroll_area)

        self.setLayout(dialog_layout)