FROM python:3.10.8-bullseye

WORKDIR ./code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip
COPY ./requirements.txt /code/
RUN pip install -r requirements.txt

COPY ./migrations.sh /code/
RUN sed -i 's/\r$//g' /code/migrations.sh
RUN chmod +x /code/migrations.sh

RUN apt-get update
RUN apt-get -y install netcat

COPY . /code/

ENTRYPOINT ["/code/migrations.sh"]