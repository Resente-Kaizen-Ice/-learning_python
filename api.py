from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Gender, Role, UserUpdate
from uuid import uuid4, UUID
from mysql.connector import Error
from database_connection import get_connection  # this is the connection string

app = FastAPI()


db: List[User] = [
    User(
        id=uuid4(),
        first_name="Kaizen Ice",
        middle_name="",
        last_name="Resente",
        gender=Gender.male,
        role=[Role.admin, Role.user],
    ),
    User(
        id=uuid4(),
        first_name="Mary Jane",
        middle_name="Arancon",
        last_name="Plaza",
        gender=Gender.female,
        role=[Role.user],
    ),
]


@app.get("/api/v1/database_users")
async def get_user_database():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM users"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return rows
    except Error as e:
        raise HTTPException(status_code=500, detail=f"{e}")


@app.get("/")
def root():
    return {"Hello": "Mundo"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404, detail=f"user with id {user_id} does not exist"
    )


@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, userupdate: UserUpdate):
    for user in db:
        if user.id == user_id:
            if user.first_name is not None:
                user.first_name = userupdate.first_name
            if user.middle_name is not None:
                user.middle_name = userupdate.middle_name
            if user.last_name is not None:
                user.last_name = userupdate.last_name
            if user.role is not None:
                user.role = userupdate.role
            return
    raise HTTPException(
        status_code=404, detail=f"user with id = {user_id} is not found"
    )
