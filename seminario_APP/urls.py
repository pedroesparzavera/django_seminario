from django.urls import path
from .views import (
    bulk_delete_inscritos,
    home,  # Asegúrate de importar la vista home
    InscritoListView, InscritoCreateView, InscritoUpdateView, 
    InscritoDeleteView, institucion_list, institucion_detail
)
from .api_views import (
    InscritoListCreateView, InscritoRetrieveView, institucion_list_api, datos_autor
)

urlpatterns = [
    # Página principal
    path('', home, name='home'),  # URL raíz apunta a la vista 'home'

    # Rutas Web
    path('inscritos/', InscritoListView.as_view(), name='inscrito_list'),
    path('inscritos/crear/', InscritoCreateView.as_view(), name='inscrito_create'),
    path('inscritos/editar/<int:pk>/', InscritoUpdateView.as_view(), name='inscrito_update'),
    path('inscritos/eliminar/<int:pk>/', InscritoDeleteView.as_view(), name='inscrito_delete'),
    path('instituciones/', institucion_list, name='institucion_list'),
    path('instituciones/<int:id>/', institucion_detail, name='institucion_detail'),
    path('inscritos/eliminar-seleccionados/', bulk_delete_inscritos, name='inscrito_bulk_delete'),
    
    # Rutas API
    path('api/inscritos/', InscritoListCreateView.as_view(), name='api_inscritos'),
    path('api/inscritos/<int:pk>/', InscritoRetrieveView.as_view(), name='api_inscrito_detail'),
    path('api/instituciones/', institucion_list_api, name='api_instituciones'),
    path('api/autor/', datos_autor, name='api_autor'),
]
