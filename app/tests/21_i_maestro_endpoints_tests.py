import pytest

@pytest.mark.django_db
def test_get_instituciones(client):
    response = client.get("/maestro/instituciones/1", content_type="application/json")
    assert response.status_code == 200
    assert response.data["nombre"] == "Clínica RedSalud Elqui"
    assert response.data["tipo"] == "clinica"
    assert response.data["titularidad"] == "privado"
    assert response.data["num_camas_uti"] == 12
    assert response.data["num_camas_uci"] == 6


@pytest.mark.django_db
def test_get_instituciones_empty(client):
    response = client.get("/maestro/instituciones/400", content_type="application/json")
    assert response.status_code == 404
    assert bool(response.data.get('detail')), "Se encuentran elementos en la query"


@pytest.mark.django_db
def test_get_instituciones_list(client):
    response = client.get("/maestro/instituciones", content_type="application/json")
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
    response = client.get("/maestro/items/1", content_type="application/json")
    assert response.status_code == 200
    assert response.data['nombre'] == 'Respirador Mecánico'
    assert response.data['tipo'] == 'soporte_vital'

@pytest.mark.django_db
def test_post_item(client):
    response = client.post(
        "/maestro/items",
        {
            "nombre": 'Item de prueba',
            "tipo": 'apoyo_monitorizacion'
        },
        content_type="application/json",
    )
    assert response.status_code == 201
    assert response.data['nombre'] == "Item de prueba"
    assert response.data['tipo'] == "apoyo_monitorizacion"

@pytest.mark.django_db
def test_get_item_list(client):
    response = client.get("/maestro/items", content_type="application/json")
    assert response.status_code == 200
    assert response.data[0]["nombre"] == 'Respirador Mecánico'
    assert response.data[0]["tipo"] == 'soporte_vital'

    assert response.data[5]["nombre"] == 'Cama de Cuidados Intensivos'
    assert response.data[5]["tipo"] == 'apoyo_monitorizacion'

    assert response.data[9]["nombre"] == 'Sistema de Infusión de Fluidos'
    assert response.data[9]["tipo"] == 'apoyo_monitorizacion'


@pytest.mark.django_db
def test_get_medicamento(client):
    response = client.get("/maestro/medicamentos/1", content_type="application/json")
    assert response.status_code == 200
    assert response.data['nombre_comercial'] == "Ibupirac"
    assert response.data['nombre_generico'] == "Ibuprofeno"
    assert response.data['ingredientes'] == "Ibuprofeno"
    assert response.data['concentracion'] == "400mg"
    assert response.data['forma_presentacion'] == "blister"
    assert response.data['forma_farmaceutica'] == "tabletas"
    assert response.data['via_administracion'] == "oral"


@pytest.mark.django_db
def test_get_medicamento_list(client):
    response = client.get("/maestro/medicamentos", content_type="application/json")
    assert response.status_code == 200
    assert len(response.data) == 35
    assert response.data[0]['nombre_comercial'] == "Ibupirac"
    assert response.data[0]['nombre_generico'] == "Ibuprofeno"
    assert response.data[0]['ingredientes'] == "Ibuprofeno"
    assert response.data[0]['concentracion'] == "400mg"
    assert response.data[0]['forma_presentacion'] == "blister"
    assert response.data[0]['forma_farmaceutica'] == "tabletas"
    assert response.data[0]['via_administracion'] == "oral"

    assert response.data[6]['nombre_comercial'] == "Veklury"
    assert response.data[6]['nombre_generico'] == "Remdesivir"
    assert response.data[6]['ingredientes'] == "Remdesivir"
    assert response.data[6]['concentracion'] == "100mg"
    assert response.data[6]['forma_presentacion'] == "ampolla"
    assert response.data[6]['forma_farmaceutica'] == "solucion"
    assert response.data[6]['via_administracion'] == "intravenoso"


@pytest.mark.django_db
def test_get_quiebre(client):
    response = client.get("/maestro/quiebres/1", content_type="application/json")
    assert response.status_code == 200
    assert response.data['medicamento'] == 5
    assert response.data['institucion'] == 1
    assert response.data['cantidad'] == 500


@pytest.mark.django_db
def test_get_quiebre_list(client):
    response = client.get("/maestro/quiebres", content_type="application/json")
    assert response.status_code == 200
    assert (len(response.data)) == 46
    assert response.data[0]['medicamento'] == 5
    assert response.data[0]['institucion'] == 1
    assert response.data[0]['cantidad'] == 500

    assert response.data[10]['medicamento'] == 17
    assert response.data[10]['institucion'] == 30
    assert response.data[10]['cantidad'] == 6000

    assert response.data[15]['medicamento'] == 9
    assert response.data[15]['institucion'] == 19
    assert response.data[15]['cantidad'] == 5000


@pytest.mark.django_db
def test_get_equipamiento_list(client):
    response = client.get("/maestro/equipamientos", content_type="application/json")
    assert response.status_code == 200
    assert len(response.data) == 20
    # TODO: validar algunos campos


@pytest.mark.django_db
def test_get_equipamiento(client):
    response = client.get("/maestro/equipamientos/4", content_type="application/json")
    assert response.status_code == 200
    #TODO: validar campo obtenido


@pytest.mark.django_db
def test_get_equipamiento_empty(client):
    response = client.get("/maestro/equipamientos/1", content_type="application/json")
    assert response.status_code == 404
    #TODO: validar campo obtenido
