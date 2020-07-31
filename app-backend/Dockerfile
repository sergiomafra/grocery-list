# Pull Python3.8 image from Docker HUB
FROM python:3.8.5-slim-buster

# Work directory
WORKDIR /srv/api

# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /srv/api
RUN pip install -r requirements.txt

# Copy API to container
COPY . /srv/api/