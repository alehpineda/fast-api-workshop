FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./app /app/app

RUN useradd -m 10000
USER 10000
