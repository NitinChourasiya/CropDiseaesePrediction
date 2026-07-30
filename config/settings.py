import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------
# API
# -------------------------

API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000"
)

# -------------------------
# Model
# -------------------------

MODEL_PATH = os.getenv(
    "MODEL_PATH",
    str(BASE_DIR / "models" / "crop_disease_cnn_v1.h5")
)

DEFAULT_MODEL = os.getenv(
    "DEFAULT_MODEL",
    "custom_cnn"
)

# -------------------------
# Database
# -------------------------

DATABASE_PATH = os.getenv(
    "DATABASE_PATH",
    str(BASE_DIR / "database" / "database.db")
)