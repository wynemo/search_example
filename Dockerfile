from python:3.11.3-slim-bullseye as builder
WORKDIR /
ENV http_proxy $http_proxy
ENV https_proxy $http_proxy
RUN python -m venv /venv
RUN apt-get update
RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential
COPY ./requirements.txt /requirements.txt
RUN /venv/bin/pip install -i https://mirrors.aliyun.com/pypi/simple/ -r /requirements.txt
ENV http_proxy=
ENV https_proxy=
from python:3.11.3-slim-bullseye
WORKDIR /
ENV http_proxy $http_proxy
ENV https_proxy $http_proxy
RUN apt-get update
RUN apt-get install -y libmariadb3
COPY --from=builder /venv venv
ENV http_proxy=
ENV https_proxy=
