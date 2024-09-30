# AQ-T1-back

Este es el backend del proyecto AQ-T1 desarrollado con **Python** y **FastAPI**, utilizando una **arquitectura hexagonal**. Este patrón de diseño permite que los componentes internos del sistema (dominio) sean independientes de los mecanismos externos (adaptadores). En caso de que se quiera consultar el frontend de este proyecto, se puede consultar el siguiente enlace:
https://github.com/andres345gm/AQ-T1-front

### Carpetas Principales:

- **adapters/**: Contiene los adaptadores que permiten que diferentes capas del sistema se comuniquen entre sí.
  - **DTOs/**: Objetos de transferencia de datos.
  - **inadpt/**: Adaptadores de entrada.
  - **out/**: Adaptadores de salida.

- **domain/**: Contiene el modelo de dominio y los puertos de la aplicación.
  - **model/**: Modelos de datos.
  - **ports/**: Interfaces para los servicios y adaptadores.

- **services/**: Implementaciones de los servicios que contienen la lógica de negocio.
  - **add_purchase_service.py**: Servicio encargado de añadir compras.
  - **login_service.py**: Servicio de autenticación y manejo de sesiones de usuario.
  - **pokemon_api_service.py**: Servicio que interactúa con la API de Pokémon.
  - **purchase_crud_service.py**: CRUD para gestionar compras.
  - **user_crud_service.py**: CRUD para gestionar usuarios.

- **Dockerfile**: Archivo para la configuración de Docker.
- **docker-compose.yml**: Archivo para levantar el proyecto usando Docker Compose.
- **requirements.txt**: Archivo que contiene las dependencias necesarias del proyecto.

## Requisitos

Antes de ejecutar este proyecto, asegúrate de tener instalado:

- **Docker** y **Docker Compose**.
- **Python 3.12** o superior.

## Instalación y Ejecución

Sigue estos pasos para levantar el proyecto:

1. **Clona el repositorio**:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd AQ-T1-back
   ```
2. **Ejecuta el proyecto**:
   ```bash
   docker-compose up --build
   ```
3. **Accede a la documentación de la API**:
    Abre tu navegador y accede a `http://localhost:8000/docs`.
