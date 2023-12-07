from django.db import models

# Create your models here.
class Libro(models.Model):
	titulo = models.CharField(max_length=200)
	autor = models.CharField(max_length=200)
	precio = models.DecimalField(max_digits=6,decimal_places=2)
	
	def __str__(self):
		return self.titulo