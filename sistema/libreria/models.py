from django.db import models

# Create your models here.
class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    anio = models.IntegerField(verbose_name="Año")
    imagen = models.ImageField(upload_to='imagenes/', verbose_name="Imagen", null=True)
    director = models.CharField(max_length=100, default="")
    resenia = models.TextField(verbose_name="Reseña", null=True)

    def __str__(self):
        fila = self.nombre + " (" + str(self.anio) + ", " + self.director + ")"
        return fila

    def delete(self, using=True, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
    

