
from fastapi import FastAPI
from app.api.v1.endpoints.health import router as health_router
from app.core.config import settings
from app.api.v1.endpoints.user import router as users_router
from app.api.v1.endpoints.auth import router as auth_router

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)
app.include_router(health_router)
app.include_router(users_router)
app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to EduGenius AI API",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }