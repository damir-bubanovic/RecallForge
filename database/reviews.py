from database.connection import get_connection


def create_review(card_id: int, rating: str):
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO review_history (
                card_id,
                rating
            )
            VALUES (?, ?)
            """,
            (
                card_id,
                rating,
            )
        )

        connection.commit()

        return cursor.lastrowid