# SearchService-Dockerfile

FROM python:3.8.0-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get -y update && apt-get install -y libpq-dev gcc
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /SearchService/
WORKDIR /SearchService


