from pydantic import BaseModel


# class ItemBase(BaseModel):
#     title: str
#     description: str | None = None


# class ItemCreate(ItemBase):
#     pass


# class Item(ItemBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True


# class UserBase(BaseModel):
#     email: str


# class UserCreate(UserBase):
#     password: str


# class User(UserBase):
#     id: int
#     is_active: bool
#     items: list[Item] = []

#     class Config:
#         orm_mode = True
#**************************************************
class CourseBase(BaseModel):
    name: str
    unit: int | None = None


class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    id: int
    student_id: int

    class Config:
        orm_mode = True


class StudentBase(BaseModel):
    firstname: str


class StudentCreate(StudentBase):
    firstname: str
    lastname: str


class Student(StudentBase):
    id: int
    graduated: bool
    courses: list[Course] = []

    class Config:
        orm_mode = True