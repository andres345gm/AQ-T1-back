# adapters/in/user_api.py
from fastapi import FastAPI, HTTPException
from typing import List
import logging

from app.adapters.out.mock_user_repository import MockUserRepository
from app.adapters.out.mongo import MongoRepository
from app.domain.use_cases.user_crud_use_case import UserCrudUseCase
from app.domain.model.user import User

# Configurar el logging
logging.basicConfig(level=logging.INFO)  # Configuración de logging
logger = logging.getLogger(__name__)


app = FastAPI()

user_repo = MockUserRepository()
user_crud = UserCrudUseCase(user_repo)


@app.post("/user", response_model=User)
def create_user(username: str, password: str):
    return user_crud.create_user(username, password)


@app.get("/user/{user_id}", response_model=User)
def get_user(user_id: int):
    logger.info(f"Buscando usuario con id {user_id}")
    user = user_crud.get_user(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


@app.put("/user/{user_id}", response_model=User)
def update_user(user_id: int, username: str, password: str):
    user = user_crud.update_user(user_id, username, password)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    if user_crud.delete_user(user_id):
        return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")


@app.get("/user", response_model=List[User])
def list_users():
    return user_crud.list_users()
