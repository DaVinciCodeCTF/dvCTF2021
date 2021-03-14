FROM ubuntu

COPY . /app/
WORKDIR /app/

RUN apt-get update && apt-get install -y python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools libmysqlclient-dev
RUN pip3 install gunicorn flask requests
RUN adduser telegram --disabled-password

USER telegram

CMD gunicorn --workers=16 --threads=16 --bind 0.0.0.0:5000 wsgi:app
