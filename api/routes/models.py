from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():

    return {
        "message": "Welcome to Crop Disease Detection API"
    }


@router.get("/models")
def get_models():

    return {
        "models": [
            "Custom CNN"
        ]
    }