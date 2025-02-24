FROM python:3.11

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r requirements.txt
