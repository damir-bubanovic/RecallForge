from database.connection import get_connection


def create_card(
    topic_id: int,
    question_text: str,
    answer_text: str,
    question_image_path: str | None = None,
    answer_image_path: str | None = None,
):
    cleaned_question = question_text.strip()
    cleaned_answer = answer_text.strip()

    if not cleaned_question:
        raise ValueError("Question text cannot be empty.")

    if not cleaned_answer:
        raise ValueError("Answer text cannot be empty.")

    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO cards (
                topic_id,
                question_text,
                answer_text,
                question_image_path,
                answer_image_path
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                topic_id,
                cleaned_question,
                cleaned_answer,
                question_image_path,
                answer_image_path,
            )
        )

        connection.commit()

        return cursor.lastrowid


def get_cards_by_topic(topic_id: int):
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
            WHERE topic_id = ?
            ORDER BY id ASC
            """,
            (topic_id,)
        )

        return cursor.fetchall()


def update_card(
    card_id: int,
    question_text: str,
    answer_text: str,
    question_image_path: str | None = None,
    answer_image_path: str | None = None,
):
    cleaned_question = question_text.strip()
    cleaned_answer = answer_text.strip()

    if not cleaned_question:
        raise ValueError("Question text cannot be empty.")

    if not cleaned_answer:
        raise ValueError("Answer text cannot be empty.")

    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE cards
            SET question_text = ?,
                answer_text = ?,
                question_image_path = ?,
                answer_image_path = ?,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """,
            (
                cleaned_question,
                cleaned_answer,
                question_image_path,
                answer_image_path,
                card_id,
            )
        )

        connection.commit()

        return cursor.rowcount


def delete_card(card_id: int):
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM cards
            WHERE id = ?
            """,
            (card_id,)
        )

        connection.commit()

        return cursor.rowcount