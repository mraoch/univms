from dataclasses import dataclass

@dataclass
class Student:
    student_id: int
    name: str
    email: str
    department: str