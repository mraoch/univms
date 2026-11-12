from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from config.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(100),
        nullable=False
    )

    age = Column(Integer)

    email = Column(
        String(200),
        nullable=False
    )