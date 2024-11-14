# Importaciones estándar de Django
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .forms import RegistroUsuarioForm

# Vista para registrar un nuevo usuario
def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save() 
            login(request, user)  # Loguear automáticamente al usuario
            messages.success(request, f'Bienvenido {user.first_name}, tu cuenta ha sido creada exitosamente.')
            return redirect('panel_principal')
        else:
            messages.error(request, 'Hubo un error al crear tu cuenta. Por favor, revisa los campos.')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'usuario/registro.html', {'form': form})

# Vista personalizada de login (login tradicional de Django)
class CustomLoginView(LoginView):
    template_name = 'usuario/login.html'

# Vista para iniciar sesión (formulario de autenticación)
def iniciar_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('panel_principal')  # Redirige al panel principal
    else:
        form = AuthenticationForm()
    return render(request, 'usuario/iniciar_sesion.html', {'form': form})

# Panel principal donde el usuario puede ver su información
@login_required
def panel_principal(request):
    return render(request, 'usuario/panel_principal.html', {'usuario': request.user})

# Vista para editar los datos del perfil del usuario
@login_required
def editar_usuario(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('panel_principal')  # Redirigir a la vista principal
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, 'usuario/editar_usuario.html', {'form': form})

# Vista para cambiar la contraseña del usuario
@login_required
def cambiar_contraseña(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Mantener la sesión activa después de cambiar la contraseña
            return redirect('panel_principal')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'usuario/cambiar_contraseña.html', {'form': form})

# Vista para cerrar la sesión del usuario
def cerrar_sesion(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('login')  # Redirige al inicio de sesión después de cerrar la sesión

# Vista para eliminar la cuenta del usuario
@login_required
def eliminar_usuario(request):
    if request.method == 'POST':
        user = request.user
        user.delete()  # Elimina la cuenta del usuario
        return redirect('login')  # Redirige a la página de login
    return render(request, 'usuario/eliminar_cuenta.html')  # Si no es POST, muestra una página de confirmación
