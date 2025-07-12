from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


@login_required
def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})


@login_required
def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tarea creada con éxito.")
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    return render(request, 'tareas/crear_tarea.html', {'form': form})


@login_required
def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.delete()
    messages.warning(request, f"Tarea '{tarea.titulo}' eliminada.")
    return redirect('lista_tareas')


@login_required
def cambiar_estado(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.completada = not tarea.completada
    tarea.save()
    estado = "completada" if tarea.completada else "pendiente"
    messages.info(request, f"Tarea marcada como {estado}.")
    return redirect('lista_tareas')


@login_required
def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            messages.success(request, "Tarea actualizada con éxito.")
            return redirect('lista_tareas')
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'tareas/editar_tarea.html', {'form': form, 'tarea': tarea})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Sesión iniciada correctamente.')
            return redirect('lista_tareas')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'tareas/login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Sesión cerrada correctamente.')
    return redirect('login')

