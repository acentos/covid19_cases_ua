FROM python:3.7.4-buster
LABEL maintainer="acentos"

ENV CONTNAME='stat_ua'

ADD . /covid19_stat
WORKDIR /covid19_stat

COPY . ./

RUN apt update \
    && apt upgrade -y \
    && apt install vim -y

RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt

CMD . venv/bin/activate && exec python app.py
