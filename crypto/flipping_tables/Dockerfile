FROM alpine

RUN apk update && apk add s6-networking python3 py3-pycryptodome
RUN adduser ecb -D
COPY flipping_tables.py secret_data.py /app/
WORKDIR /app/

EXPOSE 2000
USER ecb
CMD s6-tcpserver 0.0.0.0 2000 python3 flipping_tables.py
