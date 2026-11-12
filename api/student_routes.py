from fastapi import APIRouter
from fastapi import Depends

from config.database import get_db

from services.student_service import (
    StudentService
)

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

service = StudentService()


@router.get("/")
def get_students(
    db=Depends(get_db)
):
    return service.list_students(db)


@router.get("/{student_id}")
def get_student(
    student_id: int,
    db=Depends(get_db)
):
    return service.get_student(
        db,
        student_id
    )


@router.post("/")
def add_student(
    name: str,
    age: int,
    email: str,
    db=Depends(get_db)
):
    return service.create_student(
        db,
        name,
        age,
        email
    )


@router.delete("/{student_id}")
def delete_student(
    student_id: int,
    db=Depends(get_db)
):
    return service.delete_student(
        db,
        student_id
    )