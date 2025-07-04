from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaForm
from django.shortcuts import get_object_or_404, redirect

def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})

def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    return render(request, 'tareas/crear_tarea.html', {'form': form})

def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.delete()
    return redirect('lista_tareas')

def cambiar_estado(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.completada = not tarea.completada
    tarea.save()
    return redirect('lista_tareas')

