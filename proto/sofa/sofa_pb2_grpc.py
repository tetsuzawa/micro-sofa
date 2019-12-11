# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from proto.sofa import sofa_pb2 as proto_dot_sofa_dot_sofa__pb2


class SOFAStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.DecodeSOFA = channel.stream_stream(
        '/sample.SOFA/DecodeSOFA',
        request_serializer=proto_dot_sofa_dot_sofa__pb2.SOFANameMessage.SerializeToString,
        response_deserializer=proto_dot_sofa_dot_sofa__pb2.SOFAInfoMessage.FromString,
        )


class SOFAServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def DecodeSOFA(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SOFAServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'DecodeSOFA': grpc.stream_stream_rpc_method_handler(
          servicer.DecodeSOFA,
          request_deserializer=proto_dot_sofa_dot_sofa__pb2.SOFANameMessage.FromString,
          response_serializer=proto_dot_sofa_dot_sofa__pb2.SOFAInfoMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'sample.SOFA', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
