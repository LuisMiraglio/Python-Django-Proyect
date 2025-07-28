from django.urls import path
from .views import (
    lista_tareas,
    crear_tarea,
    editar_tarea,
    eliminar_tarea,
    cambiar_estado,
    ver_tarea,
    login_view,
    logout_view,
    registro_view,
)

urlpatterns = [
    path('', lista_tareas, name='lista_tareas'),                     # /tareas/
    path('nueva/', crear_tarea, name='crear_tarea'),                # /tareas/nueva/
    path('editar/<int:tarea_id>/', editar_tarea, name='editar_tarea'),
    path('eliminar/<int:tarea_id>/', eliminar_tarea, name='eliminar_tarea'),
    path('cambiar_estado/<int:tarea_id>/', cambiar_estado, name='cambiar_estado'),
    path('ver/<int:tarea_id>/', ver_tarea, name='ver_tarea'),

    # Autenticación
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registro/', registro_view, name='registro'),
]
