# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rastervision/protos/keras_classification/model.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rastervision/protos/keras_classification/model.proto',
  package='keras_classification.protos',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n4rastervision/protos/keras_classification/model.proto\x12\x1bkeras_classification.protos\"\xb5\x01\n\x05Model\x12\x12\n\ninput_size\x18\x01 \x02(\x05\x12\x12\n\nnb_classes\x18\x02 \x02(\x05\x12\x35\n\x04type\x18\x03 \x02(\x0e\x32\'.keras_classification.protos.Model.Type\x12\x12\n\nmodel_path\x18\x04 \x02(\t\x12#\n\x14load_weights_by_name\x18\x05 \x01(\x08:\x05\x66\x61lse\"\x14\n\x04Type\x12\x0c\n\x08RESNET50\x10\x01')
)



_MODEL_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='keras_classification.protos.Model.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESNET50', index=0, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=247,
  serialized_end=267,
)
_sym_db.RegisterEnumDescriptor(_MODEL_TYPE)


_MODEL = _descriptor.Descriptor(
  name='Model',
  full_name='keras_classification.protos.Model',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input_size', full_name='keras_classification.protos.Model.input_size', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nb_classes', full_name='keras_classification.protos.Model.nb_classes', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='keras_classification.protos.Model.type', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_path', full_name='keras_classification.protos.Model.model_path', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='load_weights_by_name', full_name='keras_classification.protos.Model.load_weights_by_name', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MODEL_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=267,
)

_MODEL.fields_by_name['type'].enum_type = _MODEL_TYPE
_MODEL_TYPE.containing_type = _MODEL
DESCRIPTOR.message_types_by_name['Model'] = _MODEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Model = _reflection.GeneratedProtocolMessageType('Model', (_message.Message,), dict(
  DESCRIPTOR = _MODEL,
  __module__ = 'rastervision.protos.keras_classification.model_pb2'
  # @@protoc_insertion_point(class_scope:keras_classification.protos.Model)
  ))
_sym_db.RegisterMessage(Model)


# @@protoc_insertion_point(module_scope)
