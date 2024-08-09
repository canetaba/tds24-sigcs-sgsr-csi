from django.urls import path

from .views import (
    InstitucionesRetrieveDestroyAPIView,
    MedicamentosRetrieveDestroyAPIView,
    ItemsRetrieveDestroyAPIView,
)

app_name = "maestro"
urlpatterns = [
    path("instituciones/<int:pk>", InstitucionesRetrieveDestroyAPIView.as_view(), name="instituciones-lc"),
    path("items/<int:pk>", ItemsRetrieveDestroyAPIView.as_view(), name="items-lc"),
    path("medicamentos/<int:pk>", MedicamentosRetrieveDestroyAPIView.as_view(), name="medicamentos-lc")
]
