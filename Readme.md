# Fake User Data API

A FastAPI-based REST API that generates realistic fake user profiles for use in frontend development, UI mockups, or testing environments.

---

## Features

- Generate fake user data including:
  - Name, username, email (real or temp)
  - Avatar
  - Gender
  - Phone number
  - Birthdate
  - Address
  - Bio
  - Job title
- Specify how many users to generate (1–100)
- Optionally set locale and use temporary email domains

---

## Tech Stack

- Python
- FastAPI
- Faker

---

## Installation

```bash
pip install fastapi uvicorn faker
uvicorn main:app --reload
```

---

## API Endpoint

### `GET /users`

Generates a list of fake user profiles.

#### Query Parameters:

| Parameter     | Type    | Default | Description                                      |
|---------------|---------|---------|--------------------------------------------------|
| `count`       | int     | 10      | Number of users to generate (1–100)             |
| `locale`      | string  | None    | Faker locale for regional data (e.g., `en`, `fr_FR`, `hi_IN`) |
| `temp_email`  | boolean | false   | If true, generates temporary email addresses    |

---

#### Example Request

```bash
http://127.0.0.1:8000/users?count=5&locale=en&temp_email=true
```