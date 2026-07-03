import numpy as np
import tensorflow as tf

from backend.services.model_loader import load_model


def model_prediction(test_image):
    """
    Predict the disease class index for an uploaded image.
    """

    model = load_model()

    image = tf.keras.preprocessing.image.load_img(
        test_image,
        target_size=(128, 128)
    )

    input_arr = tf.keras.preprocessing.image.img_to_array(image)

    input_arr = np.expand_dims(input_arr, axis=0)

    prediction = model.predict(input_arr, verbose=0)

    result_index = np.argmax(prediction)

    return result_index
    # Predict the disease