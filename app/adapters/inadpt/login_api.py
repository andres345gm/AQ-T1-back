import logging

from fastapi import APIRouter, HTTPException

from app.adapters.DTOs.login_dto import LoginDTO
from app.adapters.DTOs.user_response_dto import UserResponseDTO, map_user_to_response_dto
from app.adapters.out.singleton import singletonUserRepository
from app.domain.services.login_service import LoginUseCase


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
login_router = APIRouter()

login_use_case = LoginUseCase(singletonUserRepository)


@login_router.post("/login", response_model=UserResponseDTO)
def login(login_data: LoginDTO):
    user = login_use_case.login(login_data.user, login_data.password)
    logger.info(f"User {login_data.user} logged in")

    if user:
        user_response = map_user_to_response_dto(user)
        return user_response
    raise HTTPException(status_code=404, detail="User not found")