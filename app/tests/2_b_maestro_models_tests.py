import pytest
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

@pytest.mark.django_db
def test_institucion_model():
    from maestro.models import Institucion
    institucion = Institucion.objects.create(
    nombre = "Institucion de prueba",
    tipo = "clinica",
    titularidad = "publico",
    num_camas_uti = 2,
    num_camas_uci = 2,
    factor = 1.0
    )
    institucion.titularidad = "Titularidad no permitida"
    with pytest.raises(ValidationError):
        institucion.save()
        institucion = Institucion.objects.get(id = institucion.id)
        assert institucion.titularidad in [choice[0] for choice in Institucion.Titularidad.choices]
    pass
    institucion.full_clean()
    institucion.tipo = "Tipo no permitido"

    institucion.full_clean()
    institucion.num_camas_uci = -3
    institucion.num_camas_uti = -3
    with pytest.raises(IntegrityError):
        institucion.save()
        institucion = institucion.objects.get(id=institucion.id)
        assert institucion.num_camas_uci >= 0, "num_camas_uci debe ser mayor o igual que cero"
        assert institucion.num_camas_uti >= 0, "num_camas_uti debe ser mayor o igual que cero"
    pass

'''

@pytest.mark.django_db
def test_medicamento_model():
    from maestro.models import Medicamento
    pass


@pytest.mark.django_db
def test_item_model():
    from maestro.models import Item
    pass


@pytest.mark.django_db
def test_equipamiento_model():
    from maestro.models import Equipamiento
    pass


@pytest.mark.django_db
def test_quiebre_model():
    from maestro.models import Quiebre
    pass
'''