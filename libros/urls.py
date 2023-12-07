from .views import VistaListaLibros, VistaDetalleLibro
from django.urls import path

urlpatterns = [
path('', VistaListaLibros.as_view(), name='lista_libros'),
path('<int:pk>/', VistaDetalleLibro.as_view(), name='detalle_libro'),
]