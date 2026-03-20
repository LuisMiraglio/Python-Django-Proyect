from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Tarea
from .forms import TareaForm, RegistroForm

# ✅ Lista de tareas con filtros, búsqueda y paginación
@login_required
def lista_tareas(request):
    estado = request.GET.get("estado")
    buscar = request.GET.get("buscar", "").strip()

    # SOLO tareas del usuario logueado
    tareas = Tarea.objects.filter(user=request.user)

    if estado == "pendiente":
        tareas = tareas.filter(completada=False)
    elif estado == "completada":
        tareas = tareas.filter(completada=True)

    if buscar:
        tareas = tareas.filter(titulo__icontains=buscar)

    tareas = tareas.order_by('-id')  # Mostrar primero las más recientes

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
    form = TareaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        tarea = form.save(commit=False)
        tarea.user = request.user  # Asociar la tarea al usuario actual
        tarea.save()
        messages.success(request, "Tarea creada con éxito.")
        return redirect('lista_tareas')
    return render(request, 'tareas/crear_tarea.html', {'form': form})

# ✅ Editar tarea
@login_required
def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id, user=request.user)
    form = TareaForm(request.POST or None, instance=tarea)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Tarea actualizada con éxito.")
        return redirect('lista_tareas')
    return render(request, 'tareas/editar_tarea.html', {'form': form, 'tarea': tarea})

# ✅ Cambiar estado de completada
@login_required
def cambiar_estado(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id, user=request.user)
    tarea.completada = not tarea.completada
    tarea.save()
    estado = "completada" if tarea.completada else "pendiente"
    messages.info(request, f"Tarea marcada como {estado}.")
    return redirect('lista_tareas')

# ✅ Eliminar tarea
@login_required
def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id, user=request.user)
    tarea.delete()
    messages.warning(request, f"Tarea '{tarea.titulo}' eliminada.")
    return redirect('lista_tareas')

# ✅ Ver detalle de una tarea
@login_required
def ver_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id, user=request.user)
    return render(request, 'tareas/ver_tarea.html', {'tarea': tarea})

# ✅ Login (con vaciado de mensajes para que no quede notificación "pegada")
def login_view(request):
    # Limpiar todos los mensajes pendientes al acceder al login
    storage = messages.get_messages(request)
    list(storage)  # Vacia el storage para eliminar mensajes "pegados"

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('lista_tareas')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'tareas/login.html')

# ✅ Logout
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

# ✅ Registro de nuevos usuarios
def registro_view(request):
    form = RegistroForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Tu cuenta fue creada exitosamente. Ahora podés iniciar sesión.")
        return redirect('login')
    return render(request, "tareas/registro.html", {"form": form})
