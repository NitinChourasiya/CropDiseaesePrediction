from fastapi import APIRouter
from database.history import (
    get_prediction_history,
    get_prediction_by_id,
    delete_prediction,
    delete_all_predictions,
)

router = APIRouter()

#all history is sent as response
@router.get("/history")
def history():

    rows = get_prediction_history()

    history = []

    for row in rows:
        history.append({
            "id": row["id"],
            "timestamp": row["timestamp"],
            "model": row["model_name"],
            "disease": row["disease_name"],
            "image": row["image_name"],
            "confidence": row["confidence"],
        })

    return history

# history of only id is sent as response
@router.get("/history/{prediction_id}")
def get_history_by_id(prediction_id: int):

    row = get_prediction_by_id(prediction_id)

    if row is None:
        return {
            "message": "Prediction not found"
        }

    return {
        "id": row["id"],
        "timestamp": row["timestamp"],
        "model": row["model_name"],
        "disease": row["disease_name"],
        "image": row["image_name"],
        "confidence": row["confidence"],
    }

@router.delete("/history/{prediction_id}")
def remove_prediction(prediction_id: int):

    deleted = delete_prediction(prediction_id)

    if not deleted:
        return {
            "message": "Prediction not found"
        }

    return {
        "message": "Prediction deleted successfully"
    }

@router.delete("/history")
def remove_all_predictions():

    delete_all_predictions()

    return {
        "message": "All prediction history deleted successfully"
    }