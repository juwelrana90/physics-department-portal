# Physics Department Portal

Digital academic management platform for the Physics Department, Govt. Edward College, Pabna.

## Project goals

The platform is designed for approximately 800+ students and will eventually provide:

- Student, teacher, and administrator accounts
- Student profiles
- Course management
- Attendance tracking
- Assignments and submissions
- Events and announcements
- Notifications
- Roll-number based private/group chat
- Web and Android interfaces
- Expandable academic analytics and other department services

## Initial technology stack

- Backend: Python + FastAPI
- Database: PostgreSQL
- ORM: SQLAlchemy
- Authentication: JWT + Argon2 password hashing
- Web frontend: HTML/CSS/JavaScript starter
- Mobile frontend: Flutter starter
- API documentation: OpenAPI/Swagger through FastAPI

## Repository structure

```text
physics-department-portal/
├── backend/
├── database/
├── frontend/
│   ├── web/
│   └── mobile/
├── docs/
└── .gitignore
```

## Quick start

### 1. Backend

```bash
cd backend
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
copy .env.example .env   # Windows
# cp .env.example .env   # macOS/Linux

uvicorn app.main:app --reload
```

API will be available at:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs

### 2. PostgreSQL

Create a PostgreSQL database named `physics_portal`, then put its connection URL in `backend/.env`.

Example:

```env
DATABASE_URL=postgresql+psycopg://postgres:password@localhost:5432/physics_portal
JWT_SECRET_KEY=change-this-in-development
```

### 3. Database

For the initial schema:

```bash
psql -U postgres -d physics_portal -f database/schema.sql
```

The FastAPI backend also creates missing tables on startup during this early development stage.

## Development rule

Never commit `.env` or real passwords, student data, or production secrets.

This is an educational/development foundation. Before real departmental deployment, conduct a proper security review, backup strategy, privacy review, and authorization audit.
