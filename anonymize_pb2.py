# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: anonymize.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='anonymize.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x61nonymize.proto\" \n\x0cSendNickname\x12\x10\n\x08nickname\x18\x01 \x01(\t\"!\n\tReceiveID\x12\x14\n\x0c\x61nonymizedID\x18\x01 \x01(\x05\x32@\n\x10\x41nonymizeService\x12,\n\x0fgetAnonymizedID\x12\r.SendNickname\x1a\n.ReceiveIDb\x06proto3'
)




_SENDNICKNAME = _descriptor.Descriptor(
  name='SendNickname',
  full_name='SendNickname',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nickname', full_name='SendNickname.nickname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=19,
  serialized_end=51,
)


_RECEIVEID = _descriptor.Descriptor(
  name='ReceiveID',
  full_name='ReceiveID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='anonymizedID', full_name='ReceiveID.anonymizedID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=53,
  serialized_end=86,
)

DESCRIPTOR.message_types_by_name['SendNickname'] = _SENDNICKNAME
DESCRIPTOR.message_types_by_name['ReceiveID'] = _RECEIVEID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SendNickname = _reflection.GeneratedProtocolMessageType('SendNickname', (_message.Message,), {
  'DESCRIPTOR' : _SENDNICKNAME,
  '__module__' : 'anonymize_pb2'
  # @@protoc_insertion_point(class_scope:SendNickname)
  })
_sym_db.RegisterMessage(SendNickname)

ReceiveID = _reflection.GeneratedProtocolMessageType('ReceiveID', (_message.Message,), {
  'DESCRIPTOR' : _RECEIVEID,
  '__module__' : 'anonymize_pb2'
  # @@protoc_insertion_point(class_scope:ReceiveID)
  })
_sym_db.RegisterMessage(ReceiveID)



_ANONYMIZESERVICE = _descriptor.ServiceDescriptor(
  name='AnonymizeService',
  full_name='AnonymizeService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=88,
  serialized_end=152,
  methods=[
  _descriptor.MethodDescriptor(
    name='getAnonymizedID',
    full_name='AnonymizeService.getAnonymizedID',
    index=0,
    containing_service=None,
    input_type=_SENDNICKNAME,
    output_type=_RECEIVEID,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ANONYMIZESERVICE)

DESCRIPTOR.services_by_name['AnonymizeService'] = _ANONYMIZESERVICE

# @@protoc_insertion_point(module_scope)
