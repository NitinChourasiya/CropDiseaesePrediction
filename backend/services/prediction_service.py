import numpy as np

from backend.services.model_loader import load_model
from backend.utils.image_loader import load_image


def predict_image(image_file):

    model = load_model()

    original_image, img_array = load_image(image_file)

    prediction = model.predict(
        img_array,
        verbose=0,
    )

    result_index = np.argmax(prediction)

    confidence = float(
        prediction[0][result_index]
    )

    return {
        "model": model,
        "original_image": original_image,
        "img_array": img_array,
        "prediction": prediction,
        "result_index": result_index,
        "confidence": confidence,
    }