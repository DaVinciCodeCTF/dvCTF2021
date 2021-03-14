FROM ubuntu

COPY ./app /app/
WORKDIR /app/

RUN apt-get update && apt-get install -y python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools libmysqlclient-dev
RUN pip3 install gunicorn flask flask-mysqldb
RUN adduser lajoute --disabled-password

USER lajoute

CMD gunicorn --workers=32 --threads=32 --bind 0.0.0.0:5000 wsgi:app
