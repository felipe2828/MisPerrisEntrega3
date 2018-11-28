from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^mascotas/listar/$',views.ListaMascotas, name="ListarMascotas"),
]