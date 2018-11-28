from django.db import models

# Create your models here.
estadoMascota=[
    ('disponible', 'Disponible'),
    ('adoptado','Adoptado'),
    ('rescatado','Rescatado'),
    ]


class Mascota(models.Model):
    nombreMascota=models.CharField(max_length=20)
    razaMascota=models.CharField(max_length=20)
    descripcionMascota=models.CharField(max_length=50)
    estadoMascota = models.CharField(max_length=15,default='',choices=estadoMascota,verbose_name="estadoMascota")
    fotoMascota=models.ImageField(upload_to='Sistema/static/images/')