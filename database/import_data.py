from database.connection import get_connection


def clear_all_data():
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute("DELETE FROM review_history")
        cursor.execute("DELETE FROM cards")
        cursor.execute("DELETE FROM topics")
        cursor.execute("DELETE FROM subjects")

        connection.commit()


def import_subjects(subjects):
    subject_id_map = {}

    with get_connection() as connection:
        cursor = connection.cursor()

        for subject in subjects:
            old_id = subject["id"]

            cursor.execute(
                """
                INSERT INTO subjects (name, created_at, updated_at)
                VALUES (?, ?, ?)
                """,
                (
                    subject["name"],
                    subject.get("created_at"),
                    subject.get("updated_at"),
                ),
            )

            subject_id_map[old_id] = cursor.lastrowid

        connection.commit()

    return subject_id_map


def import_topics(topics, subject_id_map):
    topic_id_map = {}

    with get_connection() as connection:
        cursor = connection.cursor()

        for topic in topics:
            old_id = topic["id"]
            old_subject_id = topic["subject_id"]
            new_subject_id = subject_id_map[old_subject_id]

            cursor.execute(
                """
                INSERT INTO topics (subject_id, name, created_at, updated_at)
                VALUES (?, ?, ?, ?)
                """,
                (
                    new_subject_id,
                    topic["name"],
                    topic.get("created_at"),
                    topic.get("updated_at"),
                ),
            )

            topic_id_map[old_id] = cursor.lastrowid

        connection.commit()

    return topic_id_map


def import_cards(cards, topic_id_map):
    with get_connection() as connection:
        cursor = connection.cursor()

        for card in cards:
            old_topic_id = card["topic_id"]
            new_topic_id = topic_id_map[old_topic_id]

            cursor.execute(
                """
                INSERT INTO cards (
                    topic_id,
                    question_text,
                    answer_text,
                    question_image_path,
                    answer_image_path,
                    created_at,
                    updated_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    new_topic_id,
                    card["question_text"],
                    card["answer_text"],
                    card.get("question_image_path"),
                    card.get("answer_image_path"),
                    card.get("created_at"),
                    card.get("updated_at"),
                ),
            )

        connection.commit()


def import_all_data(import_data):
    subjects = import_data.get("subjects", [])
    topics = import_data.get("topics", [])
    cards = import_data.get("cards", [])

    clear_all_data()

    subject_id_map = import_subjects(subjects)
    topic_id_map = import_topics(topics, subject_id_map)
    import_cards(cards, topic_id_map)