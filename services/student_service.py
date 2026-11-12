from models.student import Student

from repositories.student_repository import (
    StudentRepository
)


class StudentService:

    def __init__(self):

        self.repo = StudentRepository()

    def create_student(
        self,
        db,
        name,
        age,
        email
    ):

        student = Student(
            name=name,
            age=age,
            email=email
        )

        return self.repo.create(
            db,
            student
        )

    def list_students(
        self,
        db
    ):
        return self.repo.get_all(db)

    def get_student(
        self,
        db,
        student_id
    ):
        return self.repo.get_by_id(
            db,
            student_id
        )

    def delete_student(
        self,
        db,
        student_id
    ):
        return self.repo.delete(
            db,
            student_id
        )