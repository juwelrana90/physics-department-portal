from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.database import Base, engine
from app.api.routes import auth, health, students

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="Backend API for the Physics Department Portal.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict this before production deployment.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Development convenience. Use migrations (Alembic) before production.
Base.metadata.create_all(bind=engine)

app.include_router(health.router, prefix="/api")
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(
    students.router,
    prefix="/api/students",
    tags=["Students"],
)

@app.get("/")
def root():
    return {
        "name": settings.app_name,
        "version": "0.1.0",
        "status": "running",
    }
