from fastapi import FastAPI
import grpc
import requests


from pb.Helloworld_pb2 import HelloRequest
import pb.Helloworld_pb2_grpc
from pb.Helloworld_pb2_grpc import GreeterStub

app = FastAPI()


@app.get("/hello")
def hello():
    r = requests.get("http://envoy:3000")
    return {r.text}