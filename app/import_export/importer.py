import json

from PySide6.QtWidgets import QFileDialog, QMessageBox

from database.import_data import import_all_data


def import_from_json(parent, refresh_callback=None):
    file_path, _ = QFileDialog.getOpenFileName(
        parent,
        "Import RecallForge Data",
        "",
        "JSON Files (*.json)",
    )

    if not file_path:
        return

    confirmation = QMessageBox.question(
        parent,
        "Import Data",
        "This will replace all current subjects, topics, and cards.\n\nContinue?",
    )

    if confirmation != QMessageBox.StandardButton.Yes:
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            import_data = json.load(file)

        validate_import_data(import_data)
        import_all_data(import_data)

        if refresh_callback is not None:
            refresh_callback()

        QMessageBox.information(
            parent,
            "Import Complete",
            "RecallForge data imported successfully.",
        )

    except Exception as error:
        QMessageBox.warning(
            parent,
            "Import Failed",
            str(error),
        )


def validate_import_data(import_data):
    if not isinstance(import_data, dict):
        raise ValueError("Invalid import file.")

    required_keys = ["subjects", "topics", "cards"]

    for key in required_keys:
        if key not in import_data:
            raise ValueError(f"Import file is missing '{key}'.")