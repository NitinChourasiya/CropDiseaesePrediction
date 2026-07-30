from config.settings import MODEL_PATH

AVAILABLE_MODELS = {
    "custom_cnn": {
        "name": "Custom CNN",
        "path": MODEL_PATH,
        "description": "Custom CNN trained on PlantVillage dataset",
    },
}


def get_available_models():
    """
    Return all registered models.
    """
    return AVAILABLE_MODELS


def get_model_info(model_key: str):
    """
    Return configuration for a specific model.
    """
    return AVAILABLE_MODELS.get(model_key)