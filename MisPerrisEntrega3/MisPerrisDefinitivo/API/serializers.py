from rest_framework import serializers
from .models import Mascota
class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'nombreMascota',
            'razaMascota',
            'descripcionMascota',
            'estadoMascota',
        )
        model=Mascota

