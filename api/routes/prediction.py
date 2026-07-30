from fastapi import APIRouter, UploadFile, File

from backend.services.prediction_service import predict_image
from backend.services.label_loader import load_labels
from backend.services.model_registry import get_available_models
from database.history import save_prediction

router = APIRouter()


@router.get("/models")
def list_models():

    models = []

    for key, value in get_available_models().items():

        models.append({
            "key": key,
            "name": value["name"],
            "description": value["description"],
        })

    return {
        "models": models
    }


@router.post("/predict")
def predict(
    image: UploadFile = File(...)
):

    result = predict_image(image.file)

    class_names = load_labels()

    disease = class_names[result["result_index"]]

    save_prediction(
        model_name="Custom CNN",
        disease_name=disease,
        image_name=image.filename,
        confidence=result["confidence"],
    )

    return {
        "model": "Custom CNN",
        "disease": disease,
        "confidence": result["confidence"],
    }