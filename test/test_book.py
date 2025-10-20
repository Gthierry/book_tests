import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()


def test_get_all_books(client):
    response = client.get("/api/books")

    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert isinstance(data, list)
    # verif nombre elements
    assert len(data) >= 3
    # verif data keys
    assert set(data[0].keys()) == {"id", "title", "author"}


def test_get_book_by_id_failed(client):
    response = client.get("/api/books/999")
    assert response.status_code == 404
    assert response.get_json()["error"] == "Livre non trouvé"


def test_get_book_by_id_success(client):
    response = client.get("/api/books/1")
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert data == {"id": 1, "title": "Harry Potter", "author": "JK Rowling"}
