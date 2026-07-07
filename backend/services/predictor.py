import numpy as np

from backend.services.model_loader import load_model
from backend.utils.image_loader import load_image


def model_prediction(test_image):
    """
    Predict disease and return everything needed for Grad-CAM.
    """

    model = load_model()

    _, img_array = load_image(test_image)

    prediction = model.predict(img_array, verbose=0)

    result_index = np.argmax(prediction)

    return model, img_array, prediction, result_index