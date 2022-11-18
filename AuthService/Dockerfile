FROM python:3.8.0-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . /AuthService/
WORKDIR /AuthService

RUN apt-get -y update && apt-get install -y libpq-dev gcc
RUN pip install --upgrade pip && python3 -m venv ./venv && pip install -r requirements.txt

