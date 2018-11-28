from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Mascota
from .serializers import MascotaSerializer
from rest_framework.renderers import TemplateHTMLRenderer
# Create your views here.
class MascotaLista(generics.ListCreateAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
 


class MascotaDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer


