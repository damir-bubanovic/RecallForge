from database.connection import get_connection


def get_card_learning_strength(card_id: int):
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                COUNT(*) AS total_reviews,
                SUM(CASE WHEN rating = 'Again' THEN 1 ELSE 0 END) AS again_count,
                SUM(CASE WHEN rating = 'Hard' THEN 1 ELSE 0 END) AS hard_count,
                SUM(CASE WHEN rating = 'Good' THEN 1 ELSE 0 END) AS good_count,
                SUM(CASE WHEN rating = 'Easy' THEN 1 ELSE 0 END) AS easy_count
            FROM review_history
            WHERE card_id = ?
            """,
            (card_id,)
        )

        row = cursor.fetchone()

        total_reviews = row["total_reviews"]
        again_count = row["again_count"] or 0
        hard_count = row["hard_count"] or 0
        good_count = row["good_count"] or 0
        easy_count = row["easy_count"] or 0

        if total_reviews == 0:
            return "New"

        positive_reviews = good_count + easy_count
        difficult_reviews = again_count + hard_count

        if again_count >= positive_reviews:
            return "Weak"

        if total_reviews >= 5 and positive_reviews > difficult_reviews:
            return "Strong"

        return "Familiar"