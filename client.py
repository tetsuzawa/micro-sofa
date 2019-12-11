#!/usr/bin/env python
# coding:utf-8

import grpc
from proto.sofa import sofa_pb2
from proto.sofa import sofa_pb2_grpc


def hello_server(stub, name):
    messages = []
    messages.append(sofa_pb2.SOFAUploadMessage(name=name, msg='Hello'))
    responses = stub.SOFADecoder(iter(messages))
    for response in responses:
        print('Received message {}'.format(response.reply_msg))


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = sofa_pb2_grpc.SampleServiceStub(channel)
        print('--Please input your name--')
        while True:
            name = input("What's your name? > ")
            hello_server(stub, name)


if __name__ == '__main__':
    run()
