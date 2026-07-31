from fastapi import APIRouter

router = APIRouter()


@router.get("/health", tags=["Health"])
def health():

    return {
        "status": "healthy",
        "service": "Plant Disease Recognition API",
        "version": "1.0.0",
    }
