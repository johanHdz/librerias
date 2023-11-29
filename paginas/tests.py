from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import VistaPaginaInicio, VistaAcercaDe

# Create your tests here.
class PruebasPaginaInicio(SimpleTestCase):
	def test_url_existe_en_ubicacion_correcta(self):
		respuesta = self.client.get('/')
		self.assertEqual(respuesta.status.code, 200)
		
	def test_nombre_url_pagina_inicio(self):
		respuesta = self.client.get(reverse('inicio'))
		self.assertEqual(respuesta.status.code, 200)
	
	def test_plantilla_pagina_inicio(self):
		respuesta = self.client.get('/')
		self.assertTemplateUsed(respuesta, 'inicio.html')
		
	def test_pagina_inicio_contiene_html_correcto(self):
		respuesta = self.client.get('/')
		self.assertContains(respuesta, 'página de inicio')
		
	def test_pagina_inicio_no_contiene_html_incorrecto (self):
		respuesta = self.client.get('/')
		self.assertNotContains(respuesta, 'Hola!!! esto no debe estar en inicio xDxDxD')
		
	def test_pagina_inicio_url_resuelve_vistapaginainicio (self):
		vista = resolve('/')
		self.assertEqual(vista.func.__name__, VistaPaginaInicio.as_view().__name__)

class PruebasAcercaDe(SimpleTestCase):
	def SetUp(self):
		url = reverse('acercade')
		self.respuesta = self.client.get(url)
		self.assertEqual(self.respuesta.status_code, 200)

	def test_codigo_estado_acercade(self):
		self.assertEqual(self.respuesta.status_code, 200)

	def test_plantilla_acercade(self):
		self.assertTemplateUsed(self.respuesta, 'acercade.html')

	def test_acerca_contenido_html_incorrecto(self):
		self.assertNotContains(self.respuesta, 'Hola! No debería estar aquí')

	def test_url_acercade_resuelve_vistaacercade(self):
		view = resolve('/acercade/')
		self.assertEqual(
			view.func.__name__, VistaAcercaDe.as_view().__name__
		)