# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rastervision/protos/class_item.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rastervision/protos/class_item.proto',
  package='rv.protos',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n$rastervision/protos/class_item.proto\x12\trv.protos\"4\n\tClassItem\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\r\n\x05\x63olor\x18\x03 \x01(\t')
)




_CLASSITEM = _descriptor.Descriptor(
  name='ClassItem',
  full_name='rv.protos.ClassItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='rv.protos.ClassItem.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='rv.protos.ClassItem.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='rv.protos.ClassItem.color', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=103,
)

DESCRIPTOR.message_types_by_name['ClassItem'] = _CLASSITEM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClassItem = _reflection.GeneratedProtocolMessageType('ClassItem', (_message.Message,), dict(
  DESCRIPTOR = _CLASSITEM,
  __module__ = 'rastervision.protos.class_item_pb2'
  # @@protoc_insertion_point(class_scope:rv.protos.ClassItem)
  ))
_sym_db.RegisterMessage(ClassItem)


# @@protoc_insertion_point(module_scope)
