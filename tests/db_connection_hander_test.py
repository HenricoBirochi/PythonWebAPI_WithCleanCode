import pytest
from src.models.connection.db_connection_handler import DbConnectionHandler

@pytest.mark.skip(reason="Test that makes a connection on database") # Ele pula esse teste
def test_db_connection_handler(): # Para voltar a rodar o teste, remova essa linha de cima
    db_conn_handler = DbConnectionHandler()

    assert db_conn_handler.session is None

    with db_conn_handler:
        assert db_conn_handler.session is not None
