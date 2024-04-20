from sqlalchemy.orm import Session

from . import models, schemas


def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def get_student_by_lastname(db: Session, lastname: str):
    return db.query(models.Student).filter(models.Student.lastname == lastname).first()


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()


def create_student(db: Session, student: schemas.StudentCreate):

    db_student = models.Student(firstname=student.firstname, lastname=student.lastname)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_student_course(db: Session, course: schemas.CourseCreate, student_id: int):
    db_item = models.Course(**course.dict(), id = student_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item