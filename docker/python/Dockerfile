FROM python:3.9.7-buster

WORKDIR /application

COPY ./requirements.txt /application/requirements.txt
COPY ./wait-for-it.sh /application/wait-for-it.sh
RUN chmod -R 0777 *
RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:9090 app:app