# Late Show API

## Overview
This is a Flask REST API for a Late Night TV show system built with MVC architecture, PostgreSQL, and JWT authentication.

## Setup Instructions

### PostgreSQL
- Create the database:
  ```sql
  CREATE DATABASE late_show_db;
  ```

### Environment Variables
- Set the following environment variables or update `server/config.py`:
  - `DATABASE_URI`: PostgreSQL connection string (e.g. `postgresql://user:password@localhost:5432/late_show_db`)
  - `SECRET_KEY`: Flask secret key
  - `JWT_SECRET_KEY`: JWT secret key

### Install Dependencies
```bash
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell
```

### Database Setup
```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python server/seed.py
```

## Running the App
```bash
flask run
```

## Authentication Flow
- `POST /register` to create a user
- `POST /login` to get JWT token
- Use `Authorization: Bearer <token>` header for protected routes

## API Routes
| Route                  | Method | Auth Required | Description                      |
|------------------------|--------|---------------|--------------------------------|
| `/register`            | POST   | No            | Register a new user             |
| `/login`               | POST   | No            | Login and get JWT token         |
| `/episodes`            | GET    | No            | List all episodes              |
| `/episodes/<int:id>`   | GET    | No            | Get episode details + appearances |
| `/episodes/<int:id>`   | DELETE | Yes           | Delete episode + appearances    |
| `/guests`              | GET    | No            | List all guests                 |
| `/appearances`         | POST   | Yes           | Create a new appearance         |

## Postman
Import `challenge-4-lateshow.postman_collection.json` to test the API.

## GitHub
Repository link: [Add your repo link here]
