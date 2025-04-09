from fastapi import FastAPI, Query
from faker import Faker
from typing import List, Optional
import random

app = FastAPI()

@app.get("/users")
def generate_users(
    count: int = Query(10, ge=1, le=100),
    locale: Optional[str] = None,
    temp_email: bool = False
) -> List[dict]:
    fake = Faker(locale) if locale else Faker()
    users = []
    for _ in range(count):
        gender = random.choice(["male", "female"])
        name = fake.name_male() if gender == "male" else fake.name_female()
        username = fake.user_name()
        domain = "mailinator.com" if temp_email else fake.free_email_domain()
        email = f"{username}@{domain}"
        user = {
            "name": name,
            "username": username,
            "email": email,
            "avatar": f"https://i.pravatar.cc/150?u={username}",
            "gender": gender,
            "phone_number": fake.phone_number(),
            "birthdate": str(fake.date_of_birth(minimum_age=18, maximum_age=60)),
            "address": fake.address(),
            "bio": fake.sentence(nb_words=10),
            "job": fake.job()
        }
        users.append(user)
    return users