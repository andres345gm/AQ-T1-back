from app.ports.use_cases.login_user_use_case import LoginUserUseCase

class UserService:
    class LoginUser(LoginUserUseCase):
        def __init__(self, user_repository):
            self.user = user_repository


        def login_user(self, username: str, password: str) -> bool:
            if self.user.user == username and self.user.password == password:
                return True
            return False