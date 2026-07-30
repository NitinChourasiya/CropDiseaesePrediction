import tensorflow as tf

from config.settings import MODEL_PATH
from backend.services.model_downloader import download_model

_model = None


def load_model():
    global _model

    if _model is None:
        download_model()
        _model = tf.keras.models.load_model(MODEL_PATH)

    return _model