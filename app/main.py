from fastapi import FastAPI
from app.database import engine
from app import models
from app.routes import task

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routes
app.include_router(task.router)

@app.get("/")
def home():
    return {"message": "Task Manager API Running"}