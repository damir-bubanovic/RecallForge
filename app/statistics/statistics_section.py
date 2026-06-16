from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QLabel,
    QVBoxLayout,
)
from app.styles.font_sizes import FONT_SIZE_SECTION_TITLE, font_size_px



class StatisticsSection(QFrame):
    def __init__(self, title: str, rows: list[tuple[str, object]], parent=None):
        super().__init__(parent)

        self.setFrameShape(QFrame.Shape.StyledPanel)

        main_layout = QVBoxLayout()

        title_label = QLabel(title)
        title_label.setStyleSheet(
            f"font-weight: bold; {font_size_px(FONT_SIZE_SECTION_TITLE)}"
        )
        main_layout.addWidget(title_label)

        grid_layout = QGridLayout()

        for row_index, (label, value) in enumerate(rows):
            name_label = QLabel(label)
            value_label = QLabel(str(value))

            grid_layout.addWidget(name_label, row_index, 0)
            grid_layout.addWidget(value_label, row_index, 1)

        main_layout.addLayout(grid_layout)

        self.setLayout(main_layout)