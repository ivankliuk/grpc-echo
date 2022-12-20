import logging
from concurrent import futures

import grpc
import grpc_echo_pb2
import grpc_echo_pb2_grpc

LOGGER_DATEFMT = "%Y-%m-%d %H:%M:%S"
LOGGER_FORMAT = "[%(asctime)s.%(msecs)03d] %(message)s"


class Echo(grpc_echo_pb2_grpc.EchoServicer):
    def Ping(self, request, context):
        payload = str(request.payload)
        invocation_metadata = str(dict(context.invocation_metadata()))
        logging.info(f"Request payload: {request} | metadatum: {invocation_metadata}")
        pong = grpc_echo_pb2.Pong(
            payload=payload, invocation_metadata=invocation_metadata
        )
        return pong


def run_server():
    logging.basicConfig(
        level=logging.INFO, datefmt=LOGGER_DATEFMT, format=LOGGER_FORMAT
    )

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    grpc_echo_pb2_grpc.add_EchoServicer_to_server(Echo(), server)
    server.add_insecure_port("0.0.0.0:9000")

    logging.info("gRPC echo server starting")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    run_server()
