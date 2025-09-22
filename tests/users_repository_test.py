import pytest
from src.models.connection.db_connection_handler import DbConnectionHandler
from src.models.repositories.users_repository import UsersRepository

@pytest.mark.skip(reason="Happens an insertion in DB in this test")
def test_users_repository():
    db_conn = DbConnectionHandler()
    users_repo = UsersRepository(db_conn)

    person_name = "Marcos"
    age = 40
    height = 7.5

    users_repo.insert_user(person_name, age, height)
    users = users_repo.select_user(person_name)
    
    assert isinstance(users, list)
    assert len(users) == 1
    assert users[0].person_name == person_name
    assert users[0].age == age
    assert users[0].height == height
