from database.connection import get_connection


def search_all(query: str):
    cleaned_query = query.strip()

    if not cleaned_query:
        return []

    search_value = f"%{cleaned_query}%"

    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                'subject' AS result_type,
                subjects.id AS result_id,
                subjects.name AS title,
                NULL AS subtitle,
                NULL AS topic_id
            FROM subjects
            WHERE subjects.name LIKE ?

            UNION ALL

            SELECT
                'topic' AS result_type,
                topics.id AS result_id,
                topics.name AS title,
                subjects.name AS subtitle,
                topics.id AS topic_id
            FROM topics
            JOIN subjects ON topics.subject_id = subjects.id
            WHERE topics.name LIKE ?

            UNION ALL

            SELECT
                'card' AS result_type,
                cards.id AS result_id,
                cards.question_text AS title,
                topics.name || ' / ' || subjects.name AS subtitle,
                cards.topic_id AS topic_id
            FROM cards
            JOIN topics ON cards.topic_id = topics.id
            JOIN subjects ON topics.subject_id = subjects.id
            WHERE cards.question_text LIKE ?
               OR cards.answer_text LIKE ?

            ORDER BY result_type, title
            """,
            (search_value, search_value, search_value, search_value),
        )

        return cursor.fetchall()