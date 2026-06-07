import json

from PySide6.QtWidgets import QFileDialog, QMessageBox

from database.export_data import get_export_data


def export_to_json(parent):
    file_path, _ = QFileDialog.getSaveFileName(
        parent,
        "Export RecallForge Data",
        "recallforge_export.json",
        "JSON Files (*.json)",
    )

    if not file_path:
        return

    if not file_path.lower().endswith(".json"):
        file_path += ".json"

    try:
        export_data = get_export_data()

        json_text = json.dumps(export_data, ensure_ascii=False, indent=2)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(json_text)

        QMessageBox.information(
            parent,
            "Export Complete",
            "RecallForge data exported successfully.",
        )

    except Exception as error:
        QMessageBox.warning(
            parent,
            "Export Failed",
            str(error),
        )