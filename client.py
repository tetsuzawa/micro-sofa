#!/usr/bin/env python
# coding:utf-8

import grpc
from proto.sofa import sofa_pb2
from proto.sofa import sofa_pb2_grpc


def sofa_request(stub, filename):
    messages = []
    messages.append(sofa_pb2.SOFANameMessage(filename=filename))
    responses = stub.DecodeSOFA(iter(messages))
    for response in responses:
        print('Received message {}'.format(response.info_msg))


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = sofa_pb2_grpc.SOFAStub(channel)
        print('--Please input your name--')
        while True:
            name = input("What is sofa file name? > ")
            sofa_request(stub, name)


if __name__ == '__main__':
    run()
