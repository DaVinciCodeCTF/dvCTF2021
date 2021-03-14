FROM ubuntu:20.04 AS builder
RUN apt update && apt install -y make build-essential gcc-multilib
WORKDIR /build/
COPY ./src/ ./
RUN make compile

FROM ubuntu:20.04
RUN apt update && apt install -y socat gcc-multilib
RUN useradd ctf
WORKDIR /app/
COPY --from=builder /build/quotebook ./
COPY ./src/flag ./
EXPOSE 4002
USER ctf
CMD socat tcp-listen:4002,reuseaddr,fork exec:./quotebook
