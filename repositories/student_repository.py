from models.student import Student


class StudentRepository:

    def create(self, db, student):

        db.add(student)

        db.commit()

        db.refresh(student)

        return student

    def get_all(self, db):

        return db.query(Student).all()

    def get_by_id(self, db, student_id):

        return (
            db.query(Student)
            .filter(Student.id == student_id)
            .first()
        )

    def delete(self, db, student_id):

        student = self.get_by_id(
            db,
            student_id
        )

        if student:

            db.delete(student)

            db.commit()

        return student