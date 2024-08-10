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
    assert response.data["nombre_comercial"] == "Ibupirac"
    assert response.data["nombre_generico"] == "Ibuprofeno"
    assert response.data["ingredientes"] == "Ibuprofeno"
    assert response.data["concentracion"] == "400mg"
    assert response.data["forma_presentacion"] == "blister"
    assert response.data["forma_farmaceutica"] == "tabletas"
    assert response.data["via_administracion"] == "oral"

    assert response.data["indicaciones_terapeuticas"] == ("Alivio temporal de dolores leves a moderados, como dolores "
                                                          "de cabeza, dolores musculares, dolor de espalda, "
                                                          "dolor de muelas, dolor menstrual y dolor de artritis.")
    assert response.data["contraindicaciones"] == ("No utilizar en caso de alergia al ibuprofeno, úlcera péptica "
                                                   "activa o hemorragia gastrointestinal, insuficiencia cardíaca "
                                                   "grave o enfermedad hepática grave.")
    assert response.data["efectos_secundarios"] == ("Algunos efectos secundarios pueden incluir malestar estomacal, "
                                                    "náuseas, vómitos, diarrea, mareos, dolor de cabeza y erupciones "
                                                    "en la piel. En casos raros, puede causar reacciones alérgicas "
                                                    "graves.")
    assert response.data["instrucciones_dosificacion"] == ("La dosis recomendada para adultos es de 400mg cada 4 a 6 "
                                                           "horas, no excediendo los 1,200mg en 24 horas. Consulte a "
                                                           "su médico para obtener instrucciones específicas.")
    assert response.data["fabricante"] == "Laboratorios Chile S.A."

    assert response.data["informacion_almacenamiento"] == ("Almacenar en un lugar fresco y seco, protegido de la luz y "
                                                           "fuera del alcance de los niños.")
    assert response.data["interacciones_medicamentosas"] == ("El ibuprofeno puede interactuar con otros medicamentos, "
                                                             "como anticoagulantes, antihipertensivos, aspirina, "
                                                             "corticosteroides y diuréticos. Consulte a su médico o "
                                                             "farmacéutico para obtener información sobre posibles "
                                                             "interacciones.")


@pytest.mark.django_db
def test_get_medicamento_list(client):
    response = client.get("/maestro/medicamento/", content_type="application/json")
    assert response.status_code == 200
    # TODO: validar algunos campos
    assert response.data[0]["nombre_comercial"] == "Ibupirac"
    assert response.data[0]["nombre_generico"] == "Ibuprofeno"
    assert response.data[0]["ingredientes"] == "Ibuprofeno"
    assert response.data[0]["concentracion"] == "400mg"
    assert response.data[0]["forma_presentacion"] == "blister"
    assert response.data[0]["forma_farmaceutica"] == "tabletas"
    assert response.data[0]["via_administracion"] == "oral"

    assert response.data[0]["indicaciones_terapeuticas"] == ("Alivio temporal de dolores leves a moderados, como dolores "
                                                          "de cabeza, dolores musculares, dolor de espalda, "
                                                          "dolor de muelas, dolor menstrual y dolor de artritis.")
    assert response.data[0]["contraindicaciones"] == ("No utilizar en caso de alergia al ibuprofeno, úlcera péptica "
                                                   "activa o hemorragia gastrointestinal, insuficiencia cardíaca "
                                                   "grave o enfermedad hepática grave.")
    assert response.data[0]["efectos_secundarios"] == ("Algunos efectos secundarios pueden incluir malestar estomacal, "
                                                    "náuseas, vómitos, diarrea, mareos, dolor de cabeza y erupciones "
                                                    "en la piel. En casos raros, puede causar reacciones alérgicas "
                                                    "graves.")
    assert response.data[0]["instrucciones_dosificacion"] == ("La dosis recomendada para adultos es de 400mg cada 4 a 6 "
                                                           "horas, no excediendo los 1,200mg en 24 horas. Consulte a "
                                                           "su médico para obtener instrucciones específicas.")
    assert response.data[0]["fabricante"] == "Laboratorios Chile S.A."

    assert response.data[0]["informacion_almacenamiento"] == ("Almacenar en un lugar fresco y seco, protegido de la luz y "
                                                           "fuera del alcance de los niños.")
    assert response.data[0]["interacciones_medicamentosas"] == ("El ibuprofeno puede interactuar con otros medicamentos, "
                                                             "como anticoagulantes, antihipertensivos, aspirina, "
                                                             "corticosteroides y diuréticos. Consulte a su médico o "
                                                             "farmacéutico para obtener información sobre posibles "
                                                             "interacciones.")


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
