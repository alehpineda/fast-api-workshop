import pytest

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_get_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensaje": "Hola Mundo!"}


@pytest.mark.parametrize("input,expected", [(1, 1), (2, 2), (3, 3)])
def test_get_items(input, expected):
    response = client.get(f"/items/{input}")
    assert response.status_code == 200
    assert response.json() == {"item_id": expected}


@pytest.mark.parametrize(
    "input,expected",
    [
        ("alexnet", "Deep Learning rifa!"),
        ("lenet", "LeCNN todas las imgs!"),
        ("resnet", "Ten los residuos"),
    ],
)
def test_get_models(input, expected):
    response = client.get(f"/models/{input}")
    assert response.status_code == 200
    assert response.json() == {"model_name": input, "mensaje": expected}
