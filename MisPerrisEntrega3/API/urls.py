from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns=[
    url(r'^$',views.MascotaLista.as_view(),name="agregarmascota"),
    url(r'^(?P<pk>[0-9]+)$',views.MascotaDetalle.as_view(),name="editarmascota"),
]
urlpatterns = format_suffix_patterns(urlpatterns)