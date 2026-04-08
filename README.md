# Task Manager API (FastAPI + Docker)

## 🚀 Features

* Create Task
* Get Tasks
* Update Task
* Delete Task

## 🛠 Tech Stack

* FastAPI
* SQLAlchemy
* SQLite
* Docker

## 📁 Project Structure

```
task_manager/
 ├── app/
 │    ├── main.py
 │    ├── models.py
 │    ├── schemas.py
 │    ├── database.py
 │    ├── routes/
 │    │     └── task.py
 ├── Dockerfile
 ├── requirements.txt
```

## ▶️ Run Locally

```bash
uvicorn app.main:app --reload
```

## 🐳 Run with Docker

```bash
docker build -t task-manager .
docker run -p 8000:8000 task-manager
```

## 📌 API Docs

http://127.0.0.1:8000/docs

## 📖 Description

This is a Task Manager REST API built using FastAPI.
It supports CRUD operations and follows a modular architecture.
The application is containerized using Docker for easy deployment.

## 👨‍💻 Author

Ganesh Kumar
