from django.views.generic import ListView, DetailView
from .models import Libro

# Create your views here.
class VistaListaLibros(ListView):
	model = Libro
	context_object_name = 'lista_libros'
	template_name = 'libros/lista_libros.html'

class VistaDetalleLibro(DetailView):
	model = Libro
	template_name = 'libros/detalle_libro.html'