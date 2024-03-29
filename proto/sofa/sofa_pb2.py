# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/sofa/sofa.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/sofa/sofa.proto',
  package='sample',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15proto/sofa/sofa.proto\x12\x06sample\"#\n\x0fSOFANameMessage\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\"#\n\x0fSOFAInfoMessage\x12\x10\n\x08info_msg\x18\x01 \x01(\t2L\n\x04SOFA\x12\x44\n\nDecodeSOFA\x12\x17.sample.SOFANameMessage\x1a\x17.sample.SOFAInfoMessage\"\x00(\x01\x30\x01\x62\x06proto3')
)




_SOFANAMEMESSAGE = _descriptor.Descriptor(
  name='SOFANameMessage',
  full_name='sample.SOFANameMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='sample.SOFANameMessage.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=68,
)


_SOFAINFOMESSAGE = _descriptor.Descriptor(
  name='SOFAInfoMessage',
  full_name='sample.SOFAInfoMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info_msg', full_name='sample.SOFAInfoMessage.info_msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=105,
)

DESCRIPTOR.message_types_by_name['SOFANameMessage'] = _SOFANAMEMESSAGE
DESCRIPTOR.message_types_by_name['SOFAInfoMessage'] = _SOFAINFOMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SOFANameMessage = _reflection.GeneratedProtocolMessageType('SOFANameMessage', (_message.Message,), {
  'DESCRIPTOR' : _SOFANAMEMESSAGE,
  '__module__' : 'proto.sofa.sofa_pb2'
  # @@protoc_insertion_point(class_scope:sample.SOFANameMessage)
  })
_sym_db.RegisterMessage(SOFANameMessage)

SOFAInfoMessage = _reflection.GeneratedProtocolMessageType('SOFAInfoMessage', (_message.Message,), {
  'DESCRIPTOR' : _SOFAINFOMESSAGE,
  '__module__' : 'proto.sofa.sofa_pb2'
  # @@protoc_insertion_point(class_scope:sample.SOFAInfoMessage)
  })
_sym_db.RegisterMessage(SOFAInfoMessage)



_SOFA = _descriptor.ServiceDescriptor(
  name='SOFA',
  full_name='sample.SOFA',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=107,
  serialized_end=183,
  methods=[
  _descriptor.MethodDescriptor(
    name='DecodeSOFA',
    full_name='sample.SOFA.DecodeSOFA',
    index=0,
    containing_service=None,
    input_type=_SOFANAMEMESSAGE,
    output_type=_SOFAINFOMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SOFA)

DESCRIPTOR.services_by_name['SOFA'] = _SOFA

# @@protoc_insertion_point(module_scope)
