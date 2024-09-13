from abc import ABC, abstractmethod

class LoginUserUseCase(ABC):
    @abstractmethod
    def login_user(self, username: str, password: str) -> bool:
        pass