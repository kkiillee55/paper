# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chatbot.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rchatbot.proto\x12\x07\x63hatbot\"\x81\x01\n\x0b\x43hatRequest\x12\x15\n\x08question\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04\x66ile\x18\x02 \x01(\x0cH\x01\x88\x01\x01\x12\x1d\n\x10\x63reate_new_model\x18\x03 \x01(\x08H\x02\x88\x01\x01\x42\x0b\n\t_questionB\x07\n\x05_fileB\x13\n\x11_create_new_model\".\n\x0c\x43hatResponse\x12\x13\n\x06\x61nswer\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_answer2D\n\x07\x43hatbot\x12\x39\n\x04\x43hat\x12\x14.chatbot.ChatRequest\x1a\x15.chatbot.ChatResponse\"\x00(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chatbot_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CHATREQUEST']._serialized_start=27
  _globals['_CHATREQUEST']._serialized_end=156
  _globals['_CHATRESPONSE']._serialized_start=158
  _globals['_CHATRESPONSE']._serialized_end=204
  _globals['_CHATBOT']._serialized_start=206
  _globals['_CHATBOT']._serialized_end=274
# @@protoc_insertion_point(module_scope)