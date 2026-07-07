from database.db import get_connection


def save_prediction(
    model_name,
    disease_name,
    image_name,
    confidence,
):
    conn = get_connection()

    conn.execute(
        """
        INSERT INTO predictions
        (model_name, disease_name, image_name, confidence)
        VALUES (?, ?, ?, ?)
        """,
        (
            model_name,
            disease_name,
            image_name,
            confidence,
        ),
    )

    conn.commit()
    conn.close()


def get_prediction_history():

    conn = get_connection()
    
    rows = conn.execute(
        """
        SELECT *
        FROM predictions
        ORDER BY timestamp DESC
        """
    ).fetchall()

    conn.close()

    return rows