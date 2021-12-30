FROM python:3.9.9-slim-bullseye

WORKDIR ~/VM_manager

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get -y install libpq-dev gcc azure-cli
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./ ./
