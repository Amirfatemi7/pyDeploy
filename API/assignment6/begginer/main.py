from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastapi import FastAPI, HTTPException, Depends


SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


Base.metadata.create_all(bind = engine)


app = FastAPI()

def get_db():
    db = SessionLocal()
    yield db
    db.close()

@app.get("/users")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(user).filter(User.id == user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return user

@app.post("/users")
def add_user(name: str, email: str, db: Session = Depends(get_db)):
    user = User(name= name, email= email)
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user

@app.delete("/users")
def remove(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="user not found")
    db.delete(user)
    db.commit()
    return {"user":"deleted"}

@app.put("/users")
def update_user(user_id: int, name: str, email: str, db: Session = Depends(get_db)):
    user = User(id = user_id, name= name, email= email)
    user = db.query(user).filter(User.id == user_id).update(user)
    if user is None:
        raise HTTPException(status_code=404, detail="user not found")
    
    db.commit()
    db.refresh(user)
    
    return user