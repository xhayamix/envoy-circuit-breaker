FROM golang:1.19-buster

ENV PROTOBUF_VERSION 3.17.3

RUN apt-get update \
    && apt-get install -y protobuf-compiler unzip --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /go_grpc
COPY . /go.mod ./go.sum ./
RUN go mod download



