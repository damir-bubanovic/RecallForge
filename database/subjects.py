from database.connection import get_connection


def create_subject(name: str):
    cleaned_name = name.strip()

    if not cleaned_name:
        raise ValueError("Subject name cannot be empty.")

    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO subjects (name)
            VALUES (?)
            """,
            (cleaned_name,)
        )

        connection.commit()

        return cursor.lastrowid


def get_subjects():
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id, name, created_at, updated_at
            FROM subjects
            ORDER BY name ASC
            """
        )

        return cursor.fetchall()


def update_subject(subject_id: int, name: str):
    cleaned_name = name.strip()

    if not cleaned_name:
        raise ValueError("Subject name cannot be empty.")

    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE subjects
            SET name = ?,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """,
            (cleaned_name, subject_id)
        )

        connection.commit()

        return cursor.rowcount


def delete_subject(subject_id: int):
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM subjects
            WHERE id = ?
            """,
            (subject_id,)
        )

        connection.commit()

        return cursor.rowcount