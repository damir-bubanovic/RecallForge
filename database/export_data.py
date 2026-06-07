from pathlib import Path

from database.connection import get_connection


BASE_DIR = Path(__file__).resolve().parent.parent


def make_relative_path(path_value):
    if not path_value:
        return None

    path = Path(path_value)

    try:
        return str(path.relative_to(BASE_DIR))
    except ValueError:
        return str(path)


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

        cards = []

        for row in cursor.fetchall():
            card = dict(row)

            card["question_image_path"] = make_relative_path(
                card["question_image_path"]
            )
            card["answer_image_path"] = make_relative_path(
                card["answer_image_path"]
            )

            cards.append(card)

        return cards


def get_export_data():
    return {
        "version": 1,
        "subjects": get_all_subjects(),
        "topics": get_all_topics(),
        "cards": get_all_cards(),
    }