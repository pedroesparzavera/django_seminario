from django.urls import path
from .views import (
    # Vistas Web
    home, bulk_delete_inscritos,
    InscritoListView, InscritoCreateView, InscritoUpdateView, InscritoDeleteView,
    institucion_list, institucion_detail, InstitucionCreateView, InstitucionUpdateView, InstitucionDeleteView,
)
from seminario_APP.api_views import (
    # Vistas API
    InscritoListCreateView, InscritoRetrieveView, datos_autor, institucion_list_api,
)

# Definición de URLs
urlpatterns = [
    # Página principal
    path('', home, name='home'),

    # Rutas Web para Inscritos
    path('inscritos/', InscritoListView.as_view(), name='inscrito_list'),
    path('inscritos/crear/', InscritoCreateView.as_view(), name='inscrito_create'),
    path('inscritos/editar/<int:pk>/', InscritoUpdateView.as_view(), name='inscrito_update'),
    path('inscritos/eliminar/<int:pk>/', InscritoDeleteView.as_view(), name='inscrito_delete'),
    path('inscritos/eliminar-seleccionados/', bulk_delete_inscritos, name='inscrito_bulk_delete'),

    # Rutas Web para Instituciones
    path('instituciones/', institucion_list, name='institucion_list'),
    path('instituciones/crear/', InstitucionCreateView.as_view(), name='institucion_create'),
    path('instituciones/<int:id>/', institucion_detail, name='institucion_detail'),
    path('instituciones/editar/<int:pk>/', InstitucionUpdateView.as_view(), name='institucion_update'),
    path('instituciones/eliminar/<int:pk>/', InstitucionDeleteView.as_view(), name='institucion_delete'),

    # Rutas API
    path('api/inscritos/', InscritoListCreateView.as_view(), name='api_inscritos'),
    path('api/inscritos/<int:pk>/', InscritoRetrieveView.as_view(), name='api_inscrito_detail'),
    path('api/instituciones/', institucion_list_api, name='api_instituciones'),
    path('api/autor/', datos_autor, name='api_autor'),
]
