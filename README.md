# TaskFlow 🧠

**TaskFlow** es una aplicación web desarrollada con Django para la gestión de tareas personales. Pensada para organizar, priorizar y visualizar tus tareas de manera simple y moderna, permitiendo que cada usuario vea y administre únicamente sus propias tareas.

## 🚀 Características principales

- **Autenticación de usuarios**: Registro, login y logout con un diseño visual moderno y seguro.
- **Gestión de tareas por usuario**: Cada usuario sólo puede ver y administrar sus propias tareas.
- **CRUD de tareas**: Crear, leer, editar y eliminar tareas fácilmente.
- **Prioridades**: Asignación de prioridades (alta, media, baja) visualmente destacadas.
- **Estados de tarea**: Completar o marcar como pendiente cada tarea con un clic.
- **Filtrado y búsqueda**: Buscar tareas por nombre y filtrar por estado (pendiente, completada, todas).
- **Vencimiento**: Agregar fecha de vencimiento opcional a cada tarea.
- **Paginación**: Navegá fácilmente por muchas tareas.
- **Confirmación visual para eliminar**: Eliminá tareas de forma segura con un modal de confirmación.
- **Diseño moderno y responsivo**: Interfaz atractiva con Bootstrap 5 y estilos personalizados.
- **Mensajes flash**: Notificaciones de éxito, error o advertencia que desaparecen automáticamente.

## 🖥️ Capturas de pantalla

![Login moderno](docs/login.png)
![Lista de tareas](docs/lista_tareas.png)
![Registro de usuario](docs/registro.png)

*Las imágenes son de ejemplo, podés agregar las tuyas en la carpeta `docs/`.*

## ⚙️ Instalación y ejecución

1. **Cloná el repositorio**
   git clone https://github.com/LuisMiraglio/Python-Django-Proyect.git
   cd Python-Django-Proyect

2. **Crear un entorno virtual (opcional pero recomendado)**
    python -m venv env

3. **Activar el entorno virtual:**
    env\Scripts\activate

4. **Instalar las dependencias:**
    pip install -r requirements.txt

5. **Aplicar migraciones de base de datos**
    python manage.py migrate

6. **(Opcional) Crear un usuario administrador**
    python manage.py createsuperuser

7. **Iniciar el servidor**
    python manage.py runserver

8. **Entrar a la aplicación**
    Abre tu navegador en http://127.0.0.1:8000/

## 🚀 Tecnologías Utilizadas
- Django

- Bootstrap 5

- HTML, CSS, JavaScript


## 👨‍💻 Autor

- [Luis Miraglio](https://github.com/LuisMiraglio)


## 📝 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más información.


