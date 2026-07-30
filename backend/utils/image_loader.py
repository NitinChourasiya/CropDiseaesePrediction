import io
import numpy as np
import tensorflow as tf


def load_image(image_file, target_size=(128, 128)):
    """
    Load and preprocess an image for prediction.

    Supports:
    - File path
    - Streamlit UploadedFile
    - FastAPI UploadFile.file (SpooledTemporaryFile)
    - BytesIO
    """

    # FastAPI UploadFile.file -> convert to BytesIO
    if hasattr(image_file, "read") and not isinstance(image_file, io.BytesIO):
        image_file = io.BytesIO(image_file.read())
        image_file.seek(0)

    image = tf.keras.preprocessing.image.load_img(
        image_file,
        target_size=target_size,
    )

    img_array = tf.keras.preprocessing.image.img_to_array(image)

    img_array = np.expand_dims(img_array, axis=0)

    return image, img_array