from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from fastapi import FastAPI, HTTPException, Depends


# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = "postgresql://amir_amir:amir123456789@localhost:5432/database_amir"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    average = Column(Float)
    graduated = Column(Boolean)
    courses = relationship("Course", back_populates="owner")

class Course(Base):
    __tablename__ = "course"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    unit = Column(Integer)


Base.metadata.create_all(bind = engine)


app = FastAPI()

def get_db():
    db = SessionLocal()
    yield db
    db.close()

@app.get("/students")
def read(user_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == user_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="student not found")
    return student

@app.post("/students")
def add(firstname: str, lastname: str, average: float, graduated:bool, course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    student = Student(firstname= firstname, lastname= lastname, average = average, graduated = graduated, courses = course) 
    db.add(student)
    db.commit()
    db.refresh(student)
    
    return student

@app.delete("/students")
def remove(user_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == user_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="student not found")
    db.delete(student)
    db.commit()
    return {"student":"deleted"}

@app.put("/students")
def update(user_id: int, firstname: str, lastname: str, average: float, graduated:bool, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == user_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="student not found")
    student.firstname = firstname
    student.lastname = lastname
    student.average = average
    student.graduated = graduated
    db.add(student)
    db.commit()
    db.refresh(student)
    
    return student


@app.get("/courses")
def read_course(couese_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == couese_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="course not found")
    return course

@app.post("/courses")
def add_course(name: str, unit: int, db: Session = Depends(get_db)):
    course = Course(name= name, unit= unit)
    db.add(course)
    db.commit()
    db.refresh(course)
    
    return course

@app.delete("/courses")
def remove_course(couese_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == couese_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="course not found")
    db.delete(course)
    db.commit()
    return {"course":"deleted"}

@app.put("/courses")
def update_course(couese_id: int, name: str, unit: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == couese_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="course not found")
    course.name = name
    course.unit = unit
    db.add(course)
    db.commit()
    db.refresh(course)
    return course