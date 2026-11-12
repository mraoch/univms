from fastapi import FastAPI

from api.student_routes import router as student_router
from config.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="University Management System"
)

app.include_router(student_router)


@app.get("/")
def health_check():
    return {
        "status": "running",
        "database": "postgresql"
    }
