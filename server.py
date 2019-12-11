#!/usr/bin/env python
# coding: utf-8

import time
from concurrent import futures

import grpc

from proto.sofa import sofa_pb2
from proto.sofa import sofa_pb2_grpc
from sofalib import sofa_decoder


class SOFAServicer(sofa_pb2_grpc.SOFAServicer):

    def __init__(self):
        pass

    def DecodeSOFA(self, request_iterator, context):
        for new_msg in request_iterator:
            reply_msgs = []
            print(f'Receive new message! [name: {new_msg.filename}]')

            info = sofa_decoder.view_info(new_msg.filename)
            reply_msgs.append(sofa_pb2.SOFAInfoMessage(info_msg=f'Information of requested sofa file: {new_msg.filename}'))
            reply_msgs.append(sofa_pb2.SOFAInfoMessage(info_msg=info))

            for message in reply_msgs:
                yield message


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sofa_pb2_grpc.add_SOFAServicer_to_server(SOFAServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    print('Starting gRPC SOFA server...')
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
