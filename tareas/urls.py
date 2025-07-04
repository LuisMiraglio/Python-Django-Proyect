from django.urls import path
from tareas.views import lista_tareas, crear_tarea
from .views import eliminar_tarea

urlpatterns = [
    path('', lista_tareas, name='lista_tareas'),  # /tareas/
    path('nueva/', crear_tarea, name='crear_tarea'),  # /tareas/nueva/
    path('eliminar/<int:tarea_id>/', eliminar_tarea, name='eliminar_tarea'),
]

