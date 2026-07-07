import cv2
import numpy as np


import cv2
import numpy as np


def overlay_heatmap(original_image, heatmap, alpha=0.4):

    if original_image is None:
        raise ValueError("Original image is None")

    if heatmap is None:
        raise ValueError("Heatmap is None")

    if not isinstance(heatmap, np.ndarray):
        heatmap = np.array(heatmap)

    if heatmap.size == 0:
        raise ValueError("Heatmap is empty")

    heatmap = cv2.resize(
        heatmap,
        (original_image.shape[1], original_image.shape[0])
    )

    heatmap = np.uint8(255 * heatmap)

    heatmap = cv2.applyColorMap(
        heatmap,
        cv2.COLORMAP_JET
    )

    overlay = cv2.addWeighted(
        original_image,
        1 - alpha,
        heatmap,
        alpha,
        0
    )

    return overlay