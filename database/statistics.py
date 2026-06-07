from database.connection import get_connection


def get_total_subjects():
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT COUNT(*) AS total
            FROM subjects
        """)

        row = cursor.fetchone()
        return row["total"]


def get_total_topics():
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT COUNT(*) AS total
            FROM topics
        """)

        row = cursor.fetchone()
        return row["total"]


def get_total_cards():
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT COUNT(*) AS total
            FROM cards
        """)

        row = cursor.fetchone()
        return row["total"]


def get_total_cards_with_images():
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT COUNT(*) AS total
            FROM cards
            WHERE question_image_path IS NOT NULL
               OR answer_image_path IS NOT NULL
        """)

        row = cursor.fetchone()
        return row["total"]


def get_basic_statistics():
    return {
        "total_subjects": get_total_subjects(),
        "total_topics": get_total_topics(),
        "total_cards": get_total_cards(),
        "total_cards_with_images": get_total_cards_with_images(),
    }