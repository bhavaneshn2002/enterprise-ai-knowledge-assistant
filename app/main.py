from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import logger
from app.api.routes.user_routes import router as user_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
)

app.include_router(user_router)


@app.on_event("startup")
def startup_event():
    logger.info("Enterprise AI Knowledge Assistant started successfully.")


@app.get("/")
def home():
    logger.info("Home endpoint accessed.")

    return {
        "message": f"Welcome to {settings.PROJECT_NAME}"
    }


@app.get("/health")
def health():
    logger.info("Health endpoint accessed.")

    return {
        "status": "healthy"
    }