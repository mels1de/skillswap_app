# SkillSwap API

## Table of Contents

* [Project Overview](#project-overview)
* [Features](#features)
* [Tech Stack](#tech-stack)
* [Prerequisites](#prerequisites)
* [Getting Started (Local)](#getting-started-local)

  * [Clone Repository](#clone-repository)
  * [Environment Variables](#environment-variables)
  * [Install Dependencies](#install-dependencies)
  * [Database Setup](#database-setup)
  * [Run Application](#run-application)
* [Docker Setup](#docker-setup)
* [Running Tests](#running-tests)
* [Project Structure](#project-structure)
* [API Documentation](#api-documentation)
* [Contributing](#contributing)
* [License](#license)

## Project Overview


<img width="415" height="931" alt="Снимок экрана 2025-07-15 194728" src="https://github.com/user-attachments/assets/21979c06-d72a-4ff6-9c87-f428a30ae379" />
<img width="1919" height="1079" alt="Снимок экрана 2025-07-15 194628" src="https://github.com/user-attachments/assets/be1862a5-0ff4-4b6f-ada7-e4bc5503bff1" />
<img width="486" height="440" alt="Снимок экрана 2025-07-15 194642" src="https://github.com/user-attachments/assets/4c2b0391-a933-4e83-b9e2-e85399fa889e" />

SkillSwap API is an asynchronous Python backend service built with FastAPI designed to facilitate a skill-sharing platform. Users can register, authenticate with JWT, and manage (create, read, delete) their skills. The project follows modern best practices, including a service layer, Alembic migrations, Docker containerization, and automated testing.

## Features

* User registration and JWT-based authentication
* Secure password hashing with bcrypt
* CRUD operations for `Skill` resource
* Pydantic model validation
* Asynchronous database interactions with SQLAlchemy and PostgreSQL
* Versioned schema migrations using Alembic
* Docker and docker-compose support for easy deployment
* Pytest-based async tests with in-memory SQLite
* Structured logging and centralized exception handling

## Tech Stack

* **Framework**: FastAPI
* **Language**: Python 3.12
* **Database**: PostgreSQL (async via asyncpg)
* **ORM**: SQLAlchemy (async)
* **Migrations**: Alembic
* **Config**: Pydantic Settings
* **Testing**: Pytest, pytest-asyncio, httpx
* **Containerization**: Docker, docker-compose
* **Security**: JWT, bcrypt (via Passlib)

## Prerequisites

* Python 3.12+
* PostgreSQL 15+
* Docker & docker-compose (for containerized setup)

## Getting Started (Local)

### Clone Repository

```bash
git clone https://github.com/your-username/skill-swap-api.git
cd skill-swap-api
```

### Environment Variables

Copy the example file and update the variables:

```bash
cp .env.example .env
# Edit .env and set DATABASE_URL and SECRET_KEY
```

```dotenv
DATABASE_URL=postgresql+asyncpg://postgres:password@localhost/skill_swap_db
SECRET_KEY=your_jwt_secret
```

### Install Dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # on Linux/macOS
.\.venv\Scripts\activate   # on Windows PowerShell
pip install -r requirements.txt
```

### Database Setup

1. Ensure PostgreSQL is running.
2. Create the database:

   ```bash
   psql -U postgres -c "CREATE DATABASE skill_swap_db;"
   ```
3. Run Alembic migrations:

   ```bash
   alembic upgrade head
   ```

### Run Application

```bash
uvicorn app.main:app --reload
```

Visit [http://localhost:8000/docs](http://localhost:8000/docs) to explore the API documentation.

## Docker Setup

Build and start services via docker-compose:

```bash
docker-compose up --build -d
```

* **db**: PostgreSQL service on port 5432
* **web**: FastAPI service on port 8000

To stop and remove containers:

```bash
docker-compose down
```

## Running Tests

Install dev dependencies:

```bash
pip install -r requirements-dev.txt
```

Run pytest:

```bash
pytest -q
```

## Project Structure

```
├── app/
│   ├── api/            # Route definitions
│   ├── core/           # Config and security
│   ├── db/             # Database, migrations
│   ├── models/         # SQLAlchemy models
│   ├── schemas/        # Pydantic schemas
│   ├── services/       # Business logic layer
│   └── main.py         # FastAPI application
├── migrations/         # Alembic migration configs
├── tests/              # Pytest test cases
├── Dockerfile          # Multi-stage build image
├── docker-compose.yml  # Local dev orchestration
├── pytest.ini          # Pytest config
├── requirements.txt    # Production dependencies
├── requirements-dev.txt# Dev dependencies
└── README.md           # Project documentation
```

## API Documentation

Interactive Swagger UI available at `/docs` (default):

* **Auth**: `/auth/register`, `/auth/login`, `/auth/me`
* **Skills**: `/skills` (GET), `/skills/{id}` (GET), `/skills` (POST), `/skills/{id}` (DELETE)

## Contributing

Contributions are welcome! Please:

1. Fork the repo
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

Ensure tests pass and follow code style (Black, Flake8, isort).

## License

This project is licensed under the [MIT License](LICENSE).
