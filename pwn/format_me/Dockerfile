FROM debian:stretch-slim AS builder
RUN apt update && apt install -y make build-essential
WORKDIR /build/
COPY ./src/ ./
RUN make compile

FROM debian:stretch-slim
RUN apt update && apt install -y socat
RUN useradd ctf
WORKDIR /app/
COPY --from=builder /build/format_me ./
EXPOSE 4002
USER ctf
CMD socat tcp-listen:4002,reuseaddr,fork exec:./format_me
