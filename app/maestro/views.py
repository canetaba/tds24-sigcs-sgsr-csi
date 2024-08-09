from rest_framework import generics

from maestro.models import Institucion, Medicamento, Item
from maestro.serializers import InstitucionSerializer, MedicamentoSerializer,ItemSerializer


class InstitucionesRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer
    http_method_names = ["delete", "get"]


class MedicamentosRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer
    http_method_names = ["delete", "get"]


class ItemsRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    http_method_names = ["delete", "get"]