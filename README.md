# Late Show API

## Overview
This is a Flask REST API for a Late Night TV show system built with MVC architecture, PostgreSQL, and JWT authentication.

## Setup Instructions

### Prerequisites
- Python 3.8+
- PostgreSQL installed and running
- pipenv for managing Python virtual environments

### PostgreSQL Setup
1. Create the database:
   ```sql
   CREATE DATABASE late_show_db;
   ```
2. Ensure you have a PostgreSQL user with access to this database.

### Environment Variables
Set the following environment variables or update `server/config.py` accordingly:
- `DATABASE_URI`: PostgreSQL connection string, e.g. `postgresql://user:password@localhost:5432/late_show_db`
- `SECRET_KEY`: Flask secret key (default provided)
- `JWT_SECRET_KEY`: JWT secret key (default provided)

### Install Dependencies
```bash
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell
```

### Database Migration and Seeding
```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python server/seed.py
```

### Running the API
```bash
flask run
```
The API will be available at `http://127.0.0.1:5000/`

## API Endpoints

| Route                  | Method | Auth Required | Description                      |
|------------------------|--------|---------------|--------------------------------|
| `/register`            | POST   | No            | Register a new user             |
| `/login`               | POST   | No            | Login and get JWT token         |
| `/episodes`            | GET    | No            | List all episodes               |
| `/episodes/<int:id>`   | GET    | No            | Get episode details + appearances |
| `/episodes/<int:id>`   | DELETE | Yes           | Delete episode + appearances    |
| `/guests`              | GET    | No            | List all guests                 |
| `/appearances`         | POST   | Yes           | Create a new appearance         |

## Authentication Flow
- Register a user via `/register`
- Login via `/login` to receive a JWT token
- Use the token in the `Authorization: Bearer <token>` header for protected routes

## Postman Collection
Import `challenge-4-lateshow.postman_collection.json` to test the API endpoints.

## GitHub Repository
[Add your repo link here]
