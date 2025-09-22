from abc import ABC, abstractmethod
from src.models.entities.users import User

class UsersRepositoryInterface(ABC):

    @abstractmethod
    def insert_user(self, person_name: str, age: int, height: float) -> None:
        pass

    @abstractmethod
    def select_user(self, person_name: str) -> list[User]:
        pass
