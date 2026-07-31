# uvicorn api.main:app --reload
from contextlib import asynccontextmanager

from fastapi import FastAPI
from api.routes.health import router as health_router
from api.routes.models import router as model_router
from api.routes.history import router as history_router
from api.routes.prediction import router as prediction_router

from database.db import initialize_database


@asynccontextmanager
async def lifespan(app: FastAPI):

    # Initialize database
    initialize_database()

    yield

    # Future cleanup (if needed)
    # close_database()
    # unload_models()


app = FastAPI(
    title="Plant Disease Recognition API",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(health_router)
app.include_router(model_router)
app.include_router(history_router)
app.include_router(prediction_router)
