FROM debian:stretch-slim AS builder
RUN apt update && apt install -y make build-essential gcc-multilib
WORKDIR /build/
COPY ./src/ ./
RUN make compile

FROM debian:stretch-slim
RUN apt update && apt install -y socat gcc-multilib
RUN useradd ctf
WORKDIR /app/
COPY --from=builder /build/kanagawa ./
COPY ./01-disable-aslr.conf /etc/sysctl.d/
COPY ./src/flag ./
EXPOSE 4002
USER ctf
CMD socat tcp-listen:4002,reuseaddr,fork exec:./kanagawa
