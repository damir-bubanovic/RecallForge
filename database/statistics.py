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


def get_total_cards_without_images():
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT COUNT(*) AS total
            FROM cards
            WHERE question_image_path IS NULL
              AND answer_image_path IS NULL
        """)

        row = cursor.fetchone()
        return row["total"]


def get_average_cards_per_topic():
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                CASE
                    WHEN COUNT(DISTINCT topics.id) = 0 THEN 0
                    ELSE ROUND(CAST(COUNT(cards.id) AS REAL) / COUNT(DISTINCT topics.id), 2)
                END AS average_cards
            FROM topics
            LEFT JOIN cards ON cards.topic_id = topics.id
        """)

        row = cursor.fetchone()
        return row["average_cards"]


def get_largest_topic_card_count():
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT COUNT(cards.id) AS total
            FROM topics
            LEFT JOIN cards ON cards.topic_id = topics.id
            GROUP BY topics.id
            ORDER BY total DESC
            LIMIT 1
        """)

        row = cursor.fetchone()
        return row["total"] if row else 0

def get_top_topics(limit: int = 5):
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                topics.name AS topic_name,
                COUNT(cards.id) AS card_count
            FROM topics
            LEFT JOIN cards
                ON cards.topic_id = topics.id
            GROUP BY topics.id
            ORDER BY card_count DESC, topics.name ASC
            LIMIT ?
            """,
            (limit,)
        )

        return cursor.fetchall()

def get_top_subjects(limit: int = 5):
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                subjects.name AS subject_name,
                COUNT(cards.id) AS card_count
            FROM subjects
            LEFT JOIN topics
                ON topics.subject_id = subjects.id
            LEFT JOIN cards
                ON cards.topic_id = topics.id
            GROUP BY subjects.id
            ORDER BY card_count DESC, subjects.name ASC
            LIMIT ?
            """,
            (limit,)
        )

        return cursor.fetchall()

def get_basic_statistics():
    return {
        "total_subjects": get_total_subjects(),
        "total_topics": get_total_topics(),
        "total_cards": get_total_cards(),
        "total_cards_with_images": get_total_cards_with_images(),
        "total_cards_without_images": get_total_cards_without_images(),
        "average_cards_per_topic": get_average_cards_per_topic(),
        "largest_topic_card_count": get_largest_topic_card_count(),
        "top_topics": get_top_topics(),
        "top_subjects": get_top_subjects(),
    }