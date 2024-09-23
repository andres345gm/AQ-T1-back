from typing import List

from fastapi import HTTPException, APIRouter

from pythonProject.app.adapters.DTOs import UserCreateDTO
from pythonProject.app.adapters.DTOs import UserResponseDTO
from pythonProject.app.adapters.out.mock_user_repository import MockUserRepository
from pythonProject.app.domain.use_cases.user_crud_use_case import UserCrudUseCase

user_router = APIRouter()

user_repo = MockUserRepository()
user_crud = UserCrudUseCase(user_repo)

# Crear un usuario (usando UserCreateDTO como entrada)
@user_router.post("/user", response_model=UserResponseDTO)
def create_user(user_data: UserCreateDTO):
    new_user = user_crud.create_user(user_data.user, user_data.password)
    return new_user  # Se devuelve el objeto User, FastAPI lo convierte a UserResponseDTO

# Obtener un usuario por ID (usando UserResponseDTO como salida)
@user_router.get("/user/{user_id}", response_model=UserResponseDTO)
def get_user(user_id: int):
    user = user_crud.get_user(user_id)
    if user:
        return user  # FastAPI convierte el objeto a UserResponseDTO
    raise HTTPException(status_code=404, detail="User not found")

# Actualizar un usuario (usando UserResponseDTO como salida)
@user_router.put("/user/{user_id}", response_model=UserResponseDTO)
def update_user(user_id: int, user_data: UserCreateDTO):
    updated_user = user_crud.update_user(user_id, user_data.user, user_data.password)
    if updated_user:
        return updated_user  # FastAPI convierte el objeto a UserResponseDTO
    raise HTTPException(status_code=404, detail="User not found")

# Eliminar un usuario
@user_router.delete("/user/{user_id}")
def delete_user(user_id: int):
    if user_crud.delete_user(user_id):
        return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

# Listar todos los usuarios (usando UserResponseDTO como salida)
@user_router.get("/user", response_model=List[UserResponseDTO])
def list_users():
    return user_crud.list_users()  # FastAPI convierte la lista de usuarios a UserResponseDTO
