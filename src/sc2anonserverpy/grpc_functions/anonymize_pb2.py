# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: anonymize.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC, 5, 29, 0, "", "anonymize.proto"
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0f\x61nonymize.proto" \n\x0cSendNickname\x12\x10\n\x08nickname\x18\x01 \x01(\t"!\n\tReceiveID\x12\x14\n\x0c\x61nonymizedID\x18\x01 \x01(\t2@\n\x10\x41nonymizeService\x12,\n\x0fgetAnonymizedID\x12\r.SendNickname\x1a\n.ReceiveIDb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "anonymize_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals["_SENDNICKNAME"]._serialized_start = 19
    _globals["_SENDNICKNAME"]._serialized_end = 51
    _globals["_RECEIVEID"]._serialized_start = 53
    _globals["_RECEIVEID"]._serialized_end = 86
    _globals["_ANONYMIZESERVICE"]._serialized_start = 88
    _globals["_ANONYMIZESERVICE"]._serialized_end = 152
# @@protoc_insertion_point(module_scope)
