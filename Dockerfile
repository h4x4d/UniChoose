FROM python:3.10.8-bullseye

WORKDIR ./code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get -y install netcat

RUN pip install --upgrade pip
COPY ./requirements.txt /code/
RUN pip install -r requirements.txt

COPY ./migrations.sh /code/
RUN ['chmod', '+x', '/code/migrations.sh']
RUN ['chmod', '+x', 'migrations.sh']


COPY . /code/

ENTRYPOINT ["/code/migrations.sh"]