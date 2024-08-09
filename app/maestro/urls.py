from django.urls import path

from .views import (
    InstitucionesRetrieveDestroyAPIView,
    MedicamentosRetrieveDestroyAPIView,
    ItemsRetrieveDestroyAPIView,
    InstitucionesListCreateView,
    ItemsListCreateView,
    MedicamentosListCreateView,
    QuiebreListCreateView,
    QuiebreRetrieveDestroyAPIView,
    EquipamientoListCreateView,
    EquipamientoRetrieveDestroyAPIView,
)

app_name = "maestro"
urlpatterns = [
    path("institucion/", InstitucionesListCreateView.as_view(), name="instituciones-lc"),
    path("institucion/<int:pk>", InstitucionesRetrieveDestroyAPIView.as_view(), name="instituciones-rud"),
    path("item/", ItemsListCreateView.as_view(), name="items-lc"),
    path("item/<int:pk>", ItemsRetrieveDestroyAPIView.as_view(), name="items-rud"),
    path("medicamento/", MedicamentosListCreateView.as_view(), name="medicamentos-lc"),
    path("medicamento/<int:pk>", MedicamentosRetrieveDestroyAPIView.as_view(), name="medicamentos-rud"),
    path("quiebre/", QuiebreListCreateView.as_view(), name="medicamentos-lc"),
    path("quiebre/<int:pk>", QuiebreRetrieveDestroyAPIView.as_view(), name="medicamentos-rud"),
    path("equipamiento/", EquipamientoListCreateView.as_view(), name="medicamentos-lc"),
    path("equipamiento/<int:pk>", EquipamientoRetrieveDestroyAPIView.as_view(), name="medicamentos-rud"),
]
