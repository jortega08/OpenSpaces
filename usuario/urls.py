from django.contrib import admin
from django.urls import path
from usuario import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='usuario/login.html'), name='login'),
    path('registro/', views.registro_usuario, name='registro_usuario'),
    path('iniciar_sesion/', LoginView.as_view(template_name='usuario/iniciar_sesion.html'), name='iniciar_sesion'),
    path('panel/', views.panel_principal, name='panel_principal'),
    path('editar_usuario/', views.editar_usuario, name='editar_usuario'),
    path('cambiar_contraseña/', views.cambiar_contraseña, name='cambiar_contraseña'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('eliminar_usuario/', views.eliminar_usuario, name='eliminar_usuario'),
]
