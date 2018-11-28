from django.conf.urls import url,include
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns=[
    url(r'^$',views.inicio,name="inicio"),
    url(r'^clientes/$',views.gestionCliente,name="gestionCliente"),
    url(r'^usuarios/$',views.gestionCliente,name="gestionUsuario"),
    url(r'^mascotas/$',views.gestionMascota,name="gestionMascota"),
    url(r'^clientes/(?P<pk>[0-9]+)/$',views.verCliente,name="verCliente"),
    url(r'^login/$',views.ingresar,name="login"),
    url(r'^salir/$',views.salir,name="salir"),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    #url(r'^mascotas/listar/$',views.ListaMascotas, name="ListarMascotas"),
    url(r'^mascotas/disponibles/$',views.listarMascotasDisponible,name="listarMascotasDisponible"),
    url(r'^mascotas/editar/(?P<pk>[0-9]+)/$',views.editarRescatado,name="editarRescatado"),
    url(r'^mascotas/eliminar/(?P<pk>[0-9]+)/$',views.eliminarRescatado,name="eliminarRescatado"),
    path(r'base_layout',views.base_layout,name='base_layout'),
    path(r'getdata/',views.getdata,name='getdata'),

    url(r'^solicitud/(?P<pk>[0-9]+)/$',views.solicitud,name="solicitud"),

    url(r'^password_recuperar/$',auth_views.PasswordResetView.as_view(
      template_name='password_reset_form.html',
      email_template_name='password_reset_email.html',),name='password_reset',),

    url(r'^password_recuperar/hecho/$',
        auth_views.PasswordResetDoneView.as_view(
      template_name='password_reset_done.html',),name='password_reset_done',),

    url(
        r'^password_recuperar/hecho/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        #[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}
        auth_views.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy('inicio'),
            post_reset_login=True,
            template_name='password_reset_confirm.html',
            post_reset_login_backend=(
                'django.contrib.auth.backends.AllowAllUsersModelBackend'
            ),
        ),
        name='password_reset_confirm',
    ), 

    url(r'^password_recuperar/hecho/listo/$',
        auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html',),name='password_reset_complete',), 
]

urlpatterns += staticfiles_urlpatterns()
