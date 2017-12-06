FROM python:3.6.1

MAINTAINER Guizion Labs <contato@guizion.com>

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get install binutils libproj-dev gdal-bin -y --force-yes

RUN apt-get install -y locales locales-all

ENV LC_ALL pt_BR.UTF-8
ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR.UTF-8

RUN mkdir -p /app

COPY . /app

RUN pip install --no-cache-dir -r /app/crud_ws/config/requirements/local.txt

WORKDIR /app
