# LookupService-Dockerfile

FROM python:3.8.0-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /LookupService

RUN apt-get update 
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /LookupService/