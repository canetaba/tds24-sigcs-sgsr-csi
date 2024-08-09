import pytest

@pytest.mark.django_db
def test_get_instituciones(client):
    response = client.get("/maestro/instituciones/1", content_type="application/json")
    print("Response ", response.data)
    assert response.status_code == 200
    assert response.data["nombre"] == "Clínica RedSalud Elqui"
    assert response.data["tipo"] == "clinica"
    assert response.data["titularidad"] == "privado"
    assert response.data["num_camas_uti"] == 12
    assert response.data["num_camas_uci"] == 6


@pytest.mark.django_db
def test_get_instituciones_empty(client):
    response = client.get("/maestro/instituciones/400", content_type="application/json")
    print("Response ", response.data)
    assert response.status_code == 404

@pytest.mark.django_db
def test_get_item(client):
    response = client.get("/maestro/items/1", content_type="application/json")
    print("Response ", response.data)
    assert response.status_code == 200

@pytest.mark.django_db
def test_get_item(client):
    response = client.get("/maestro/medicamentos/1", content_type="application/json")
    print("Response ", response.data)
    assert response.status_code == 200