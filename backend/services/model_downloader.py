from pathlib import Path

from huggingface_hub import hf_hub_download

MODEL_NAME = "crop_disease_cnn_v1.h5"
REPO_ID = "NitinChourasiya/crop-disease-cnn"


def download_model() -> str:
    model_dir = Path("models")
    model_dir.mkdir(parents=True, exist_ok=True)

    model_path = model_dir / MODEL_NAME

    if model_path.exists():
        print(f" Model already exists: {model_path}")
        return str(model_path)

    print("Downloading model from Hugging Face...")

    downloaded_file = hf_hub_download(
        repo_id=REPO_ID,
        filename=MODEL_NAME,
        local_dir=model_dir,
    )

    print("Model downloaded successfully.")

    return downloaded_file