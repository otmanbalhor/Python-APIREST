# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.10-alpine as builder
EXPOSE 8080
WORKDIR /app

RUN apk update
RUN apk add \
    pkgconfig \
    gcc \
    musl-dev \
    bash \
    mariadb-dev

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENTRYPOINT ["python3"]

CMD ["manage.py","runserver","0.0.0.0:8080"]