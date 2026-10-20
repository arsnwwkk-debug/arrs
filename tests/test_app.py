import pytest
from app import app, requests_db

@pytest.fixture()
def client():
    app.config["TESTING"] = True
        requests_db.clear()
            with app.test_client() as client:
                    yield client
                        requests_db.clear()

                        def test_health(client):
                            response = client.get("/health")
                                assert response.status_code == 200
                                    assert response.json["status"] == "healthy"

                                    def test_create_request(client):
                                        response = client.post("/api/requests", json={
                                                "title": "Компьютерді тексеру",
                                                        "category": "computer",
                                                                "priority": "medium",
                                                                        "description": "Жұмысын тексеру"
                                                                            })
                                                                                assert response.status_code == 201
                                                                                    assert response.json["id"] == 1
                                                                                    