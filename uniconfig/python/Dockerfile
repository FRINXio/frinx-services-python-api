FROM python:3.11-buster

RUN : \
	&& apt-get -y update \
	&& apt-get -y upgrade \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /home/app
COPY . .

RUN pip3 install poetry && \
    poetry install

ENTRYPOINT '/home/app/generate.sh'

