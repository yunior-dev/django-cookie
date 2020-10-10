FROM python:3.8-alpine

LABEL authors="{{ cookiecutter.author_name }}"

ENV PYTHONUNBUFFERED 1

COPY ./requirements/development.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev zlib-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
  gcc libc-dev linux-headers postgresql-dev
RUN pip install -r requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /web
WORKDIR /web
COPY . /web

RUN adduser -D dockeruser
RUN chown -R dockeruser:dockeruser /web
RUN chmod -R 755 /web
USER dockeruser
