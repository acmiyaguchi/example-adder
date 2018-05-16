# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
FROM python:3.6-slim
MAINTAINER acmiyaguchi <acmiyaguchi@gmail.com>

RUN pip install --upgrade pip
RUN pip install pipenv

WORKDIR /app
COPY . /app

RUN pipenv sync
CMD pipenv run ./adder.py

