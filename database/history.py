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

def get_prediction_by_id(prediction_id):

    conn = get_connection()

    row = conn.execute(
        """
        SELECT *
        FROM predictions
        WHERE id = ?
        """,
        (prediction_id,)
    ).fetchone()

    conn.close()

    return row

def delete_prediction(prediction_id):

    conn = get_connection()

    cursor = conn.execute(
        """
        DELETE FROM predictions
        WHERE id = ?
        """,
        (prediction_id,)
    )

    conn.commit()

    deleted = cursor.rowcount

    conn.close()

    return deleted > 0

def delete_all_predictions():

    conn = get_connection()

    conn.execute(
        """
        DELETE FROM predictions
        """
    )

    conn.commit()

    conn.close()