import requests
from config.settings import API_URL
import os
BASE_URL = API_URL
def predict(image_file):

    files = {
        "image": (
            os.path.basename(image_file.name),
            image_file,
            "image/jpeg",
        )
    }

    try:

        response = requests.post(
            f"{BASE_URL}/predict",
            files=files,
            timeout=30,
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.ConnectionError:

        raise RuntimeError(
            "Cannot connect to FastAPI backend. "
            "Please start the server."
        )

    except requests.exceptions.Timeout:

        raise RuntimeError(
            "Prediction request timed out."
        )

    except requests.exceptions.HTTPError as e:

        raise RuntimeError(
            f"Backend returned an error: {e}"
        )
    
def get_history():

    response = requests.get(
        f"{BASE_URL}/history",
        timeout=10,
    )

    response.raise_for_status()

    return response.json()


def delete_prediction(prediction_id):

    response = requests.delete(
        f"{BASE_URL}/history/{prediction_id}",
        timeout=10,
    )

    response.raise_for_status()

    return response.json()

def delete_all_history():

    response = requests.delete(
        f"{BASE_URL}/history",
        timeout=10,
    )

    response.raise_for_status()

    return response.json()