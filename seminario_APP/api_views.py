from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Inscrito, Institucion
from .serializers import InscritoSerializer, InstitucionSerializer

@api_view(['GET'])
def institucion_detail_api(request, id):
    institucion = get_object_or_404(Institucion, id=id)
    serializer = InstitucionSerializer(institucion)
    return Response(serializer.data)




# API para listar y crear Inscritos
class InscritoListCreateView(ListCreateAPIView):
    queryset = Inscrito.objects.all()
    serializer_class = InscritoSerializer

# API para obtener un inscrito por ID
class InscritoRetrieveView(RetrieveAPIView):
    queryset = Inscrito.objects.all()
    serializer_class = InscritoSerializer

# API para listar Instituciones
@api_view(['GET'])
def institucion_list_api(request):
    instituciones = Institucion.objects.all()
    serializer = InstitucionSerializer(instituciones, many=True)
    return Response(serializer.data)

# API para datos del autor
@api_view(['GET'])
def datos_autor(request):
    autor = {
        "nombre": "Pedro Esparza",
        "proyecto": "Sistema de Inscripciones Seminario Gastronómico",
        "version": "1.0"
    }
    return Response(autor)
