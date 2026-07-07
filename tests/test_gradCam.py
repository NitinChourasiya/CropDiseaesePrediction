import cv2
import numpy as np
import tensorflow as tf

from backend.explainability.gradcam import generate_gradcam
from backend.explainability.visualization import overlay_heatmap


# -----------------------------
# Configuration
# -----------------------------
MODEL_PATH = "model_epoch_05.h5"
IMAGE_PATH = r"C:\Users\Lenovo\Documents\CropDiseaseDetectionDataset\New Plant Diseases Dataset(Augmented)\test\test\Apple___Apple_scab.JPG"      # Replace with an actual leaf image
LAST_CONV_LAYER = "conv2d_7"

# -----------------------------
# Load Model
# -----------------------------
model = tf.keras.models.load_model(MODEL_PATH)

# -----------------------------
# Load Original Image
# -----------------------------
original = cv2.imread(IMAGE_PATH)
original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)

# -----------------------------
# Prepare Model Input
# -----------------------------
img = cv2.resize(original, (128, 128))
img = img.astype(np.float32)
img = np.expand_dims(img, axis=0)

# -----------------------------
# Generate Heatmap
# -----------------------------
heatmap = generate_gradcam(
    model,
    img,
    LAST_CONV_LAYER
)

# -----------------------------
# Overlay
# -----------------------------
overlay = overlay_heatmap(original, heatmap)

# -----------------------------
# Save Output
# -----------------------------
cv2.imwrite(
    "gradcam_result.jpg",
    cv2.cvtColor(overlay, cv2.COLOR_RGB2BGR)
)

print("Grad-CAM image saved successfully.")