# app/main.py
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Modelos de datos usando Pydantic
class User(BaseModel):
    id: Optional[int] = None  # Hacer que el ID sea opcional para la creación
    username: str
    email: str
    full_name: Optional[str] = None

# Base de datos simulada para usuarios
users_db = [
    User(id=1, username="user1", email="user1@example.com", full_name="User One"),
    User(id=2, username="user2", email="user2@example.com", full_name="User Two"),
]

#Operaciones CRUD para usuarios (Create,Read,Update,Delete)
#Devuelve la base de datos con todos los usuarios
@app.get("/users/", response_model=List[User])
async def read_users():
    return users_db

#Devuelve un usuario obtieniendo su ID
@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

#Crea un usuario
@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    user.id = len(users_db) + 1
    users_db.append(user)
    return user

#Actualiza un usuario obtieniendo su ID
@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    for u in users_db:
        if u.id == user_id:
            u.username = user.username
            u.email = user.email
            u.full_name = user.full_name
            return u
    raise HTTPException(status_code=404, detail="User not found")

#Elimina un usuario obtieniendo su ID
@app.delete("/users/{user_id}", response_model=User)
async def delete_user(user_id: int):
    for i, user in enumerate(users_db):
        if user.id == user_id:
            del users_db[i]
            return user
    raise HTTPException(status_code=404, detail="User not found")
