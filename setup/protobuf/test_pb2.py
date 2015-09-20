# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test.proto',
  package='protobuf_json_test',
  serialized_pb=_b('\n\ntest.proto\x12\x12protobuf_json_test\"\xad\x01\n\x0bTestMessage\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04\x66lag\x18\x03 \x01(\x08\x12>\n\x0bnested_msgs\x18\x06 \x03(\x0b\x32).protobuf_json_test.TestMessage.NestedMsg\x12\x0f\n\x07rep_int\x18\x07 \x03(\x05\x1a\x33\n\tNestedMsg\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TESTMESSAGE_NESTEDMSG = _descriptor.Descriptor(
  name='NestedMsg',
  full_name='protobuf_json_test.TestMessage.NestedMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='protobuf_json_test.TestMessage.NestedMsg.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='protobuf_json_test.TestMessage.NestedMsg.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='protobuf_json_test.TestMessage.NestedMsg.url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=208,
)

_TESTMESSAGE = _descriptor.Descriptor(
  name='TestMessage',
  full_name='protobuf_json_test.TestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='protobuf_json_test.TestMessage.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flag', full_name='protobuf_json_test.TestMessage.flag', index=1,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nested_msgs', full_name='protobuf_json_test.TestMessage.nested_msgs', index=2,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rep_int', full_name='protobuf_json_test.TestMessage.rep_int', index=3,
      number=7, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TESTMESSAGE_NESTEDMSG, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=208,
)

_TESTMESSAGE_NESTEDMSG.containing_type = _TESTMESSAGE
_TESTMESSAGE.fields_by_name['nested_msgs'].message_type = _TESTMESSAGE_NESTEDMSG
DESCRIPTOR.message_types_by_name['TestMessage'] = _TESTMESSAGE

TestMessage = _reflection.GeneratedProtocolMessageType('TestMessage', (_message.Message,), dict(

  NestedMsg = _reflection.GeneratedProtocolMessageType('NestedMsg', (_message.Message,), dict(
    DESCRIPTOR = _TESTMESSAGE_NESTEDMSG,
    __module__ = 'test_pb2'
    # @@protoc_insertion_point(class_scope:protobuf_json_test.TestMessage.NestedMsg)
    ))
  ,
  DESCRIPTOR = _TESTMESSAGE,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_json_test.TestMessage)
  ))
_sym_db.RegisterMessage(TestMessage)
_sym_db.RegisterMessage(TestMessage.NestedMsg)


# @@protoc_insertion_point(module_scope)