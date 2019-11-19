# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rastervision/protos/tf_object_detection/graph_rewriter.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rastervision/protos/tf_object_detection/graph_rewriter.proto',
  package='rastervision.protos.tf_object_detection',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n<rastervision/protos/tf_object_detection/graph_rewriter.proto\x12\'rastervision.protos.tf_object_detection\"\\\n\rGraphRewriter\x12K\n\x0cquantization\x18\x01 \x01(\x0b\x32\x35.rastervision.protos.tf_object_detection.Quantization\"Y\n\x0cQuantization\x12\x15\n\x05\x64\x65lay\x18\x01 \x01(\x05:\x06\x35\x30\x30\x30\x30\x30\x12\x16\n\x0bweight_bits\x18\x02 \x01(\x05:\x01\x38\x12\x1a\n\x0f\x61\x63tivation_bits\x18\x03 \x01(\x05:\x01\x38')
)




_GRAPHREWRITER = _descriptor.Descriptor(
  name='GraphRewriter',
  full_name='rastervision.protos.tf_object_detection.GraphRewriter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quantization', full_name='rastervision.protos.tf_object_detection.GraphRewriter.quantization', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=105,
  serialized_end=197,
)


_QUANTIZATION = _descriptor.Descriptor(
  name='Quantization',
  full_name='rastervision.protos.tf_object_detection.Quantization',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='delay', full_name='rastervision.protos.tf_object_detection.Quantization.delay', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=500000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight_bits', full_name='rastervision.protos.tf_object_detection.Quantization.weight_bits', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=8,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activation_bits', full_name='rastervision.protos.tf_object_detection.Quantization.activation_bits', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=8,
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
  serialized_start=199,
  serialized_end=288,
)

_GRAPHREWRITER.fields_by_name['quantization'].message_type = _QUANTIZATION
DESCRIPTOR.message_types_by_name['GraphRewriter'] = _GRAPHREWRITER
DESCRIPTOR.message_types_by_name['Quantization'] = _QUANTIZATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GraphRewriter = _reflection.GeneratedProtocolMessageType('GraphRewriter', (_message.Message,), dict(
  DESCRIPTOR = _GRAPHREWRITER,
  __module__ = 'rastervision.protos.tf_object_detection.graph_rewriter_pb2'
  # @@protoc_insertion_point(class_scope:rastervision.protos.tf_object_detection.GraphRewriter)
  ))
_sym_db.RegisterMessage(GraphRewriter)

Quantization = _reflection.GeneratedProtocolMessageType('Quantization', (_message.Message,), dict(
  DESCRIPTOR = _QUANTIZATION,
  __module__ = 'rastervision.protos.tf_object_detection.graph_rewriter_pb2'
  # @@protoc_insertion_point(class_scope:rastervision.protos.tf_object_detection.Quantization)
  ))
_sym_db.RegisterMessage(Quantization)


# @@protoc_insertion_point(module_scope)
