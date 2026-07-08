from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import logger

# Import Routers
from app.api.routes.user_routes import router as user_router
from app.api.routes.auth_routes import router as auth_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
)

# Register Routers
app.include_router(user_router)
app.include_router(auth_router)


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