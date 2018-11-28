from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    codigoCliente = models.AutoField(primary_key=True)
    telefono=models.CharField(max_length=20)
    fec_nac= models.CharField(max_length=30, blank=True)
    region= models.CharField(max_length=30, blank=True)
    ciudad= models.CharField(max_length=30, blank=True)
    tipo_vivienda= models.CharField(max_length=30, blank=True)

#@receiver(post_save, sender=User)
#def update_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Cliente.objects.create(user=instance)
#    instance.cliente.save()



estadoMascota=[
    ('disponible', 'Disponible'),
    ('adoptado','Adoptado'),
    ('rescatado','Rescatado'),
    ]

class Mascota(models.Model):
    codigoMascota=models.AutoField(primary_key=True)
    nombreMascota=models.CharField(max_length=20)
    razaMascota=models.CharField(max_length=20)
    descripcionMascota=models.CharField(max_length=50)
    estadoMascota = models.CharField(max_length=15, blank=True, default='',choices=estadoMascota,verbose_name="estadoMascota")
    fotoMascota=models.ImageField(upload_to='Sistema/static/images/')

class MascotaCliente(models.Model):
    codigoMascota=models.ForeignKey(Mascota,on_delete=models.CASCADE)
    codigoCliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)