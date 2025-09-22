import pytest
from src.controllers.user_finder import UserFinder
from src.models.entities.users import User

class UserRepositoryMock:
    def __init__(self):
        self.select_user_att = {}

    def select_user(self, person_name: str) -> list:
        self.select_user_att["person_name"] = person_name
        return [
            User(
                id=123,
                person_name="John Doe",
                age=30,
                height=1.75
            )
        ]

class UserRepositoryMockWithError:
    def __init__(self):
        self.select_user_att = {}

    def select_user(self, person_name: str) -> list:
        self.select_user_att["person_name"] = person_name
        return []

def test_find_by_person_name():
    user_repository = UserRepositoryMock()
    user_finder = UserFinder(user_repository)

    person_name = "John Doe"

    response = user_finder.find_by_person_name(person_name)

    assert isinstance(response, dict)
    assert "Type" in response
    assert isinstance(response["attributes"], list)

def test_find_by_person_name_with_error():
    user_repository = UserRepositoryMockWithError()
    user_finder = UserFinder(user_repository)

    person_name = "John Doe"

    with pytest.raises(Exception) as exc_info:
        user_finder.find_by_person_name(person_name)

    assert str(exc_info.value) == "Usuario nao encontrado"
