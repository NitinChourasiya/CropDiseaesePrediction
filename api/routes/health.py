from fastapi import APIRouter

router = APIRouter()


@router.get("/health", tags=["Health"])
def health():

    return {
        "status": "healthy",
        "service": "Crop Disease Detection API",
        "version": "1.0.0",
    }