from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface

class UserCreator:
    def __init__(self, users_repository: UsersRepositoryInterface): # Inversão de dependência - D do SOLID
        self.__users_repo = users_repository
