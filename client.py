import grpc

import grpc_echo_pb2
import grpc_echo_pb2_grpc


def run_client():
    with grpc.insecure_channel("localhost:9000") as channel:
        stub = grpc_echo_pb2_grpc.EchoStub(channel)
        content = grpc_echo_pb2.Content(payload="some payload")
        response = stub.Ping(content)
    print(
        f"Ping client received following from server: {response.payload} | {response.invocation_metadata}"
    )


if __name__ == "__main__":
    run_client()
