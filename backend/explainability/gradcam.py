import numpy as np

from tf_keras_vis.gradcam import Gradcam
from tf_keras_vis.utils.model_modifiers import ReplaceToLinear
from tf_keras_vis.utils.scores import CategoricalScore


def generate_gradcam(
    model,
    img_array,
    class_index,
    last_conv_layer_name="conv2d_7",
):
    """
    Generate Grad-CAM using tf-keras-vis.
    """

    gradcam = Gradcam(
        model,
        model_modifier=ReplaceToLinear(),
        clone=True,
    )

    score = CategoricalScore(class_index)

    cam = gradcam(
        score,
        img_array,
        penultimate_layer=last_conv_layer_name,
    )

    heatmap = cam[0]

    heatmap = np.maximum(heatmap, 0)

    heatmap /= (heatmap.max() + 1e-8)

    return heatmap