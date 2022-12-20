FROM python:3.10
ADD server.py grpc_echo_pb2.py grpc_echo_pb2_grpc.py requirements.txt .
RUN pip3 install -r requirements.txt
CMD ["python3", "./server.py"]
