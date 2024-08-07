# CMS basado en Microservicios

## Microservicio de Comentarios

Este microservicio permite a los usuarios agregar, leer, actualizar y eliminar comentarios en los posts.

### Instalación

1. Clonar el repositorio.
2. Crear y activar un entorno virtual.
3. Instalar las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Aplicar las migraciones:

    ```bash
    python manage.py migrate
    ```

5. Iniciar el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

### Endpoints

- `GET /api/comments/`: Lista todos los comentarios.
- `POST /api/comments/`: Crea un nuevo comentario.
- `GET /api/comments/<id>/`: Obtiene un comentario por su ID.
- `PUT /api/comments/<id>/`: Actualiza un comentario por su ID.
- `DELETE /api/comments/<id>/`: Elimina un comentario por su ID.

### Dependencias

- Django
- Django REST framework
