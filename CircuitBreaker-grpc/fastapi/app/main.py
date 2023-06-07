from fastapi import FastAPI
import grpc


from pb.Helloworld_pb2 import HelloRequest
import pb.Helloworld_pb2_grpc
from pb.Helloworld_pb2_grpc import GreeterStub

app = FastAPI()


@app.get("/hello")
def hello(name: str):
    # gRPC client for making RPC calls to the server
    channel = grpc.insecure_channel("envoy:3000")
    client = GreeterStub(channel)
    request = HelloRequest(name=name)
    response = client.SayHello(request)

    data = {
        "message": response.message,
    }
    return data