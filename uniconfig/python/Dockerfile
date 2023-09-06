FROM python:3.10-buster

RUN apt-get -y update && \
	apt-get -y upgrade && \
	rm -rf /var/lib/apt/lists/*

WORKDIR "/home/app"

RUN pip3 install poetry
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN poetry config virtualenvs.create false
