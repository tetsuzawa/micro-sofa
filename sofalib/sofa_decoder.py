# coding: utf-8

from proto.sofa import sofa_pb2
from proto.sofa import sofa_pb2_grpc


class SampleServiceServicer(sofa_pb2_grpc.SampleServiceServicer):

    def __init__(self):
        pass

    def SOFADecoder(self, request_iterator, context):
        for new_msg in request_iterator:
            reply_msgs = []
            print('Receive new message! [name: {}, msg: {}]'.format(new_msg.name, new_msg.msg))
            reply_msgs.append(sofa_pb2.SOFAInfoMessage(reply_msg='{} {}'.format(new_msg.msg, new_msg.name)))
            reply_msgs.append(sofa_pb2.SOFAInfoMessage(reply_msg='Nice to meet you!!!'))
            for message in reply_msgs:
                yield message