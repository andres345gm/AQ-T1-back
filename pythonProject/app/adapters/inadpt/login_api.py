from fastapi import APIRouter

from pythonProject.app.adapters.DTOs.login_dto import LoginDTO
from pythonProject.app.adapters.out.mock_user_repository import MockUserRepository
from pythonProject.app.domain.use_cases.login_use_case import LoginUseCase

login_router = APIRouter()

login_repo = MockUserRepository()
login_use_case = LoginUseCase(login_repo)

@login_router.post("/login", response_model=bool)
def login(login_data: LoginDTO):
    return login_use_case.login(login_data.user, login_data.password)

