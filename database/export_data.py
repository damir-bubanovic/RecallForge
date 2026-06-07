from database.connection import get_connection


def get_all_subjects():
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id, name, created_at, updated_at
            FROM subjects
            ORDER BY id ASC
            """
        )

        return [dict(row) for row in cursor.fetchall()]


def get_all_topics():
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id, subject_id, name, created_at, updated_at
            FROM topics
            ORDER BY id ASC
            """
        )

        return [dict(row) for row in cursor.fetchall()]


def get_all_cards():
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                topic_id,
                question_text,
                answer_text,
                question_image_path,
                answer_image_path,
                created_at,
                updated_at
            FROM cards
            ORDER BY id ASC
            """
        )

        return [dict(row) for row in cursor.fetchall()]


def get_export_data():
    return {
        "version": 1,
        "subjects": get_all_subjects(),
        "topics": get_all_topics(),
        "cards": get_all_cards(),
    }