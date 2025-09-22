import pytest
from src.controllers.user_creator import UserCreator

# Isso aqui pode ser considerado um teste unitario porque voce nao usa um banco de dados real
# Apenas usa o que esta aqui dentro e a classe que voce quer testar
#classe Mock
class UserRepositoryMock:
    def insert_user(self, person_name: str, age: int, height: float) -> None:
        return

    def select_user(self, person_name: str) -> list:
        return []

class UserRepositoryMockWithError:
    def insert_user(self, person_name: str, age: int, height: float) -> None:
        return

    def select_user(self, person_name: str) -> list:
        return [1, 2, 3]  # Simula que o usuario ja existe


def test_insert_new_user():
    user_repository = UserRepositoryMock()
    user_creator = UserCreator(user_repository)

    person_name = "John Doe"
    age = 30
    height = 1.75

    response = user_creator.insert_new_user(person_name, age, height)

    assert isinstance(response, dict)
    assert "Type" in response
    assert response["count"] == 1
    assert response["message"] == "Usuario cadastrado com sucesso!"

def test_insert_new_user_with_error():
    user_repository = UserRepositoryMockWithError()
    user_creator = UserCreator(user_repository)

    with pytest.raises(Exception) as exc_info:
        user_creator.insert_new_user("Jane Doe", 25, 1.65)

    assert str(exc_info.value) == "Usuario ja cadastrado"
