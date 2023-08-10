from django import views
from django.urls import path
from .views import PostCreacion, TecladoDetalle, TecladoUpdate, TecladoDelete, LoginPagina, RegistroPagina, UsuarioEdicion, CambioPassword, HomeView, ComentarioPagina
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('login/', LoginPagina.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='base/logout.html'), name='logout'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),

    path('tecladoDetalle/<int:pk>/', TecladoDetalle.as_view(), name='teclado'),

    path('tecladoEdicion/<int:pk>/', TecladoUpdate.as_view(), name='teclado_editar'),

    path('tecladoBorrado/<int:pk>/', TecladoDelete.as_view(), name='teclado_eliminar'),

    path('postCreacion/', PostCreacion.as_view(), name='nuevo'),

    path('tecladoDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
]
