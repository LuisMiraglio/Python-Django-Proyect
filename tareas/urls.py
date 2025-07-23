from django.urls import path
from tareas.views import lista_tareas, crear_tarea
from .views import eliminar_tarea
from .views import lista_tareas, crear_tarea, eliminar_tarea, cambiar_estado, editar_tarea
from .views import login_view
from .views import logout_view
from .views import ver_tarea



urlpatterns = [
    path('', lista_tareas, name='lista_tareas'),  # /tareas/
    path('nueva/', crear_tarea, name='crear_tarea'),  # /tareas/nueva/
    path('eliminar/<int:tarea_id>/', eliminar_tarea, name='eliminar_tarea'),
    path('cambiar_estado/<int:tarea_id>/', cambiar_estado, name='cambiar_estado'),
    path('editar/<int:tarea_id>/', editar_tarea, name='editar_tarea'),
    path('ver/<int:tarea_id>/', ver_tarea, name='ver_tarea'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),


]

