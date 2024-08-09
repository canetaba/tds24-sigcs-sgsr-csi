import pytest

@pytest.mark.django_db
def test_get_instituciones(client):
    response = client.get("/maestro/institucion/1", content_type="application/json")
    print("Response ", response.data)
    assert response.status_code == 200
    assert response.data["nombre"] == "Clínica RedSalud Elqui"
    assert response.data["tipo"] == "clinica"
    assert response.data["titularidad"] == "privado"
    assert response.data["num_camas_uti"] == 12
    assert response.data["num_camas_uci"] == 6


@pytest.mark.django_db
def test_get_instituciones_empty(client):
    response = client.get("/maestro/institucion/400", content_type="application/json")
    assert response.status_code == 404


@pytest.mark.django_db
def test_get_instituciones_list(client):
    response = client.get("/maestro/institucion/", content_type="application/json")
    assert response.status_code == 200
    assert response.data[0]["nombre"] == 'Clínica RedSalud Elqui'
    assert response.data[0]["tipo"] == 'clinica'
    assert response.data[0]["titularidad"] == 'privado'
    assert response.data[0]["num_camas_uti"] == 12
    assert response.data[0]["num_camas_uci"] == 6

    assert response.data[21]["nombre"] == 'Centro de Salud Familiar Puente Alto'
    assert response.data[21]["tipo"] == 'cesfam'
    assert response.data[21]["titularidad"] == 'publico'
    assert response.data[21]["num_camas_uti"] == 8
    assert response.data[21]["num_camas_uci"] == 4

    assert response.data[33]["nombre"] == 'Centro Médico Ñuñoa'
    assert response.data[33]["tipo"] == 'centro_medico'
    assert response.data[33]["titularidad"] == 'privado'
    assert response.data[33]["num_camas_uti"] == 12
    assert response.data[33]["num_camas_uci"] == 6

    assert response.data[34]["nombre"] == 'CENABAST'
    assert response.data[34]["tipo"] == 'farmacia'
    assert response.data[34]["titularidad"] == 'publico'
    assert response.data[34]["num_camas_uti"] == 0
    assert response.data[34]["num_camas_uci"] == 0


@pytest.mark.django_db
def test_get_item(client):
    response = client.get("/maestro/item/1", content_type="application/json")
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_item_list(client):
    response = client.get("/maestro/item/", content_type="application/json")
    assert response.status_code == 200
    assert response.data[0]["nombre"] == 'Respirador Mecánico'
    assert response.data[0]["tipo"] == 'soporte_vital'

    assert response.data[5]["nombre"] == 'Cama de Cuidados Intensivos'
    assert response.data[5]["tipo"] == 'apoyo_monitorizacion'

    assert response.data[9]["nombre"] == 'Sistema de Infusión de Fluidos'
    assert response.data[9]["tipo"] == 'apoyo_monitorizacion'


@pytest.mark.django_db
def test_get_medicamento(client):
    response = client.get("/maestro/medicamento/1", content_type="application/json")
    assert response.status_code == 200
    #TODO: validar campo obtenido


@pytest.mark.django_db
def test_get_medicamento_list(client):
    response = client.get("/maestro/medicamento/", content_type="application/json")
    assert response.status_code == 200
    # TODO: validar algunos campos


@pytest.mark.django_db
def test_get_quiebre(client):
    response = client.get("/maestro/quiebre/1", content_type="application/json")
    assert response.status_code == 200
    #TODO: validar campo obtenido

@pytest.mark.django_db
def test_get_quiebre_list(client):
    response = client.get("/maestro/quiebre/", content_type="application/json")
    assert response.status_code == 200
    # TODO: validar algunos campos

@pytest.mark.django_db
def test_get_equipamiento_list(client):
    response = client.get("/maestro/equipamiento/", content_type="application/json")
    assert response.status_code == 200
    # TODO: validar algunos campos


@pytest.mark.django_db
def test_get_equipamiento(client):
    response = client.get("/maestro/equipamiento/4", content_type="application/json")
    assert response.status_code == 200
    #TODO: validar campo obtenido


@pytest.mark.django_db
def test_get_equipamiento_empty(client):
    response = client.get("/maestro/equipamiento/1", content_type="application/json")
    assert response.status_code == 404
    #TODO: validar campo obtenido
