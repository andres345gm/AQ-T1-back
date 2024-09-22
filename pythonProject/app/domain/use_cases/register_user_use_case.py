from abc import ABC, abstractmethod

class RegisterUserUseCase(ABC):
    @abstractmethod
    def register_user(self, username: str, password: str) -> bool:
        pass
