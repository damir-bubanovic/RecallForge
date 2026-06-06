from database.connection import get_connection


def create_subfolder(subject_id: int, name: str):
    cleaned_name = name.strip()

    if not cleaned_name:
        raise ValueError("Subfolder name cannot be empty.")

    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO subfolders (subject_id, name)
            VALUES (?, ?)
            """,
            (subject_id, cleaned_name)
        )

        connection.commit()

        return cursor.lastrowid


def get_subfolders_by_subject(subject_id: int):
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id, subject_id, name, created_at, updated_at
            FROM subfolders
            WHERE subject_id = ?
            ORDER BY name ASC
            """,
            (subject_id,)
        )

        return cursor.fetchall()


def update_subfolder(subfolder_id: int, name: str):
    cleaned_name = name.strip()

    if not cleaned_name:
        raise ValueError("Subfolder name cannot be empty.")

    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE subfolders
            SET name = ?,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """,
            (cleaned_name, subfolder_id)
        )

        connection.commit()

        return cursor.rowcount


def delete_subfolder(subfolder_id: int):
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM subfolders
            WHERE id = ?
            """,
            (subfolder_id,)
        )

        connection.commit()

        return cursor.rowcount