FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

LABEL org.opencontainers.image.source https://github.com/alehpineda/fastapi_test

COPY ./app /app/app

RUN useradd -m 10000
USER 10000
