import numpy as np
import tensorflow as tf


def load_image(image_file, target_size=(128, 128)):
    """
    Load and preprocess an image for model prediction.

    Args:
        image_file: Uploaded image or image path.
        target_size: Model input size.

    Returns:
        Original image (PIL.Image)
        Preprocessed numpy array of shape (1, H, W, 3)
    """

    image = tf.keras.preprocessing.image.load_img(
        image_file,
        target_size=target_size
    )

    img_array = tf.keras.preprocessing.image.img_to_array(image)

    img_array = np.expand_dims(img_array, axis=0)

    return image, img_array