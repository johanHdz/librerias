from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.
class PruebasUsuarios(TestCase):
    def test_crear_usuario(self):
        Usuario = get_user_model()
        usuario = Usuario.objects.create_user(
            username = 'Pepe',
            email = 'email@prueba.com',
            password = 'admin123'
        )
        self.assertEqual(usuario.username, 'Pepe')
        self.assertEqual(usuario.email, 'email@prueba.com')
        self.assertTrue(usuario.is_active)
        self.assertFalse(usuario.is_staff)
        self.assertFalse(usuario.is_superuser)

    def test_crear_usuario_admin(self):
        Usuario = get_user_model()
        usuario = Usuario.objects.create_superuser(
            username = 'admin',
            email = 'admin@prueba.com',
            password = 'admin123'
        )
        self.assertEqual(usuario.username, 'admin')
        self.assertEqual(usuario.email, 'admin@prueba.com')
        self.assertTrue(usuario.is_active)
        self.assertFalse(usuario.is_staff)
        self.assertFalse(usuario.is_superuser)

class pruebasPaginasRegistro(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.respuesta = self.client.get(url)
    
    def test_plantilla_registro(self):
        self.assertEqual(self.respuesta.status_code, 200)
        self.assertTemplateUsed(self.respuesta, 'registration/signup.html')
        self.assertNotContains(self.respuesta, 'Hola! No debería de estar en esta página')
        self.assertContains(self.respuesta, 'Registro')