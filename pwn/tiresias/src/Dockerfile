FROM debian:stretch-slim AS builder
RUN apt update && apt install -y make build-essential gcc-multilib
WORKDIR /build/
COPY tiresias.c Makefile ./
RUN make compile

FROM debian:stretch-slim
RUN apt update && apt install -y socat gcc-multilib
RUN useradd ctf
WORKDIR /app/
COPY --from=builder /build/tiresias ./
COPY flag ./
EXPOSE 4002
USER ctf
CMD socat tcp-listen:4002,reuseaddr,fork exec:./tiresias
