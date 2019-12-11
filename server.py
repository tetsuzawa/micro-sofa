#!/usr/bin/env python
# coding: utf-8

import time
from concurrent import futures
import grpc
from proto.sofa import sofa_pb2
from proto.sofa import sofa_pb2_grpc
from sofalib.sofa_decoder import SampleServiceServicer


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sofa_pb2_grpc.add_SampleServiceServicer_to_server(SampleServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Starting gRPC sample server...')
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
