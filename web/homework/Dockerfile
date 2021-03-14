FROM markdown-image

RUN apt update && apt install -y gunicorn3 python3-flask

COPY ./app /app/

RUN adduser homework --disabled-password

RUN mkdir -p /app/rscripts/
RUN chown homework:homework /app/rscripts/

USER root
COPY ./rscripts /app/rscripts/

WORKDIR /app/

USER homework

CMD gunicorn --workers=16 --threads=16 --bind 0.0.0.0:5000 wsgi:app
