FROM alpine

RUN apk update && apk add s6-networking python3
RUN adduser numbers -D
COPY ./app/ /app/
WORKDIR /app/

EXPOSE 2000
USER numbers
CMD s6-tcpserver 0.0.0.0 2000 python3 guess.py 
