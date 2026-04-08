from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional

from app import models, schemas
from app.database import SessionLocal

router = APIRouter()   # ✅ only this

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Task
@router.post("/tasks", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Get Tasks (with filter)
@router.get("/tasks")
def get_tasks(completed: Optional[bool] = None, db: Session = Depends(get_db)):
    if completed is not None:
        return db.query(models.Task).filter(models.Task.completed == completed).all()
    return db.query(models.Task).all()

# Update Task
@router.put("/tasks/{id}")
def update_task(id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == id).first()
    task.completed = True
    db.commit()
    return {"message": "Task updated"}

# Delete Task
@router.delete("/tasks/{id}")
def delete_task(id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == id).first()
    db.delete(task)
    db.commit()
    return {"message": "Task deleted"}