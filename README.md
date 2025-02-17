# App Fibonacci

Este proyecto es una API para calcular números de Fibonacci, desarrollada con Python y FastAPI.

## Requisitos

- Python 3.10+
- FastAPI
- Uvicorn

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/app-fibonacci.git
    cd app-fibonacci
    ```

2. Crea un entorno virtual y actívalo:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Configura las variables de entorno en un archivo .env:
    ```bash
    APP_NAME="Fibonacci API"
    API_VERSION="/api/v1"

    SECRET_KEY=
    ALGORITHM="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

## Uso

1. Inicia el servidor en modo desarrollo:
    ```bash
    uvicorn main:app --reload
    ```
    o
    ```bash
    fastapi dev main.py --reload
    ```

    flags que puedes usar "--reload", "--host", "0.0.0.0", "--port", "8000"

2. Abre tu navegador y ve a `http://127.0.0.1:8000/docs` para ver la documentación interactiva de la API.

## Endpoints

- `GET /fibonacci/{n}`: Devuelve el n-ésimo número de Fibonacci.

## Ejemplo de solicitud

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/fibonacci/10' \
  -H 'accept: application/json'
```

## Contribuir

1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.


## Docker

Para iniciar la aplicación usando Docker, sigue estos pasos:

1. Construye la imagen de Docker:
    ```bash
    comando: docker build -t <imagen> <ruta-archivo-dockerfile>
    docker build -t app-fibonacci .
    ```
Inicia un contenedor con la imagen creada:
2. I
    ```bash
    comando: docker run -d -p 8000:8000 --name <nombre_contenedor> <nombre_imagen>
    docker run -d -p 8000:8000 --name app-fibonacci-container app-fibonacci
    ```

3. Abre tu navegador y ve a `http://127.0.0.1:8000/docs` para ver la documentación interactiva de la API.

Para detener y eliminar el contenedor, usa los siguientes comandos:
```bash
docker stop app-fibonacci-container
docker rm app-fibonacci-container
```