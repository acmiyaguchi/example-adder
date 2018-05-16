FROM python:3.6-slim
MAINTAINER acmiyaguchi <acmiyaguchi@gmail.com>

RUN pip install --upgrade pip
RUN pip install pipenv

WORKDIR /app
COPY . /app

RUN pipenv sync
CMD pipenv run ./adder.py

