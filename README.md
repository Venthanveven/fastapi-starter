# FastAPI Starter Template

Reusable FastAPI backend starter for Python projects.

## Features

- FastAPI
- MySQL
- SQLAlchemy
- JWT Authentication
- Argon2 Password Hashing
- User Registration and Login
- User CRUD APIs
- Layered Architecture

## Setup

1. Create virtual environment.
2. Install dependencies:

   pip install -r backend/requirements.txt

3. Configure backend/.env using backend/.env.example.

4. Run the backend:

   cd backend
   uvicorn app.main:app --reload

5. Open API documentation:

   http://127.0.0.1:8000/docs
