# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_echo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0fgrpc_echo.proto\x12\tgrpc_echo"\x1a\n\x07\x43ontent\x12\x0f\n\x07payload\x18\x01 \x01(\t"4\n\x04Pong\x12\x0f\n\x07payload\x18\x01 \x01(\t\x12\x1b\n\x13invocation_metadata\x18\x02 \x01(\t25\n\x04\x45\x63ho\x12-\n\x04Ping\x12\x12.grpc_echo.Content\x1a\x0f.grpc_echo.Pong"\x00\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "grpc_echo_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _CONTENT._serialized_start = 30
    _CONTENT._serialized_end = 56
    _PONG._serialized_start = 58
    _PONG._serialized_end = 110
    _ECHO._serialized_start = 112
    _ECHO._serialized_end = 165
# @@protoc_insertion_point(module_scope)