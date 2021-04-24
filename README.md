# fast-api-workshop
Fast-api workshop para Flisol 2021

## Requisitos previos

- Instalar python
- Instalar docker
- Instalar git
- Cuenta en Github
- Cuenta en DockerHub
- Cuenta en Heroku

## Instrucciones:

- Descarga este repositorio
- Instala las librerias dentro de `requirements_local.txt`

```bash
pip install -r requirements_local.txt
```

- Para correr el servidor local

```bash
uvicorn app.main:app --reload
```

- En el navegador visita localhost:8000 (El puerto default)

- Tambien, visita localhost:8000/docs para ver la documentacion.

- Correr la herramienta de calidad de codigo `flake8`.

```bash
flake8
```

- Para correr las pruebas unitarias en local

```bash
pytest
```

- Construir imagen del contenedor local

```bash
docker image build -t fast_api_workshop .
```

- Correr contenedor de manera local

```
docker container run -d -p 8000:80 fast_api_workshop
```
