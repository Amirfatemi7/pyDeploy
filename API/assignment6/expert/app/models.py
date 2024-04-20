from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)

#     items = relationship("Item", back_populates="owner")


# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")

class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    average = Column(Float, index=True)
    graduated = Column(Boolean, default=True)
    courses = relationship("Course", back_populates="student")

class Course(Base):
    __tablename__ = "course"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    unit = Column(Integer, index=True)
    student_id = Column(Integer, ForeignKey("student.id"))
    student = relationship("Student", back_populates="courses")