from database.connection import get_connection


def create_topic(subject_id: int, name: str):
    cleaned_name = name.strip()

    if not cleaned_name:
        raise ValueError("Topic name cannot be empty.")

    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO topics (subject_id, name)
            VALUES (?, ?)
            """,
            (subject_id, cleaned_name)
        )

        connection.commit()

        return cursor.lastrowid


def get_topics_by_subject(subject_id: int):
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id, subject_id, name, created_at, updated_at
            FROM topics
            WHERE subject_id = ?
            ORDER BY name ASC
            """,
            (subject_id,)
        )

        return cursor.fetchall()


def update_topic(topic_id: int, name: str):
    cleaned_name = name.strip()

    if not cleaned_name:
        raise ValueError("Topic name cannot be empty.")

    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE topics
            SET name = ?,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """,
            (cleaned_name, topic_id)
        )

        connection.commit()

        return cursor.rowcount


def delete_topic(topic_id: int):
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM topics
            WHERE id = ?
            """,
            (topic_id,)
        )

        connection.commit()

        return cursor.rowcount