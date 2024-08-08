from rest_framework import generics
from .models import Movimiento, Consumo
from .serializers import MovimientoSerializer, ConsumoSerializer


class MovimientoListCreateView(generics.ListCreateAPIView):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer
    http_method_names = ["post", "get"]


class MovimientoRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer
    http_method_names = ["delete", "get"]


class MovimientoLoteRetrieveView:
    pass


class MovimientoMedicamentoView:
    def get():
        pass


class ConsumoListCreateView(generics.ListCreateAPIView):
    queryset = Consumo.objects.all()
    serializer_class = ConsumoSerializer
    http_method_names = ["post", "get"]


class ConsumoRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Consumo.objects.all()
    serializer_class = ConsumoSerializer
    http_method_names = ["delete", "get"]
