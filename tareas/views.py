from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.core.paginator import Paginator

@login_required
def lista_tareas(request):
    estado = request.GET.get("estado")
    buscar = request.GET.get("buscar", "").strip()

    tareas = Tarea.objects.all()

    if estado == "pendiente":
        tareas = tareas.filter(completada=False)
    elif estado == "completada":
        tareas = tareas.filter(completada=True)

    if buscar:
        tareas = tareas.filter(titulo__icontains=buscar)

    # ✅ Ordenar de forma consistente
    tareas = tareas.order_by('-id')  # o 'creada' si tenés ese campo

    # ✅ Paginación
    paginator = Paginator(tareas, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'tareas/lista_tareas.html', {
        'tareas': page_obj,
        'page_obj': page_obj,
        'estado': estado,
        'buscar': buscar,
    })

# ✅ Crear tarea
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

# ✅ Eliminar tarea
@login_required
def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.delete()
    messages.warning(request, f"Tarea '{tarea.titulo}' eliminada.")
    return redirect('lista_tareas')

# ✅ Cambiar estado de completada
@login_required
def cambiar_estado(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.completada = not tarea.completada
    tarea.save()
    estado = "completada" if tarea.completada else "pendiente"
    messages.info(request, f"Tarea marcada como {estado}.")
    return redirect('lista_tareas')

# ✅ Editar tarea
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

# ✅ Login
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

# ✅ Logout
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Sesión cerrada correctamente.')
    return redirect('login')
