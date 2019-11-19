# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rastervision/protos/tf_object_detection/hyperparams.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rastervision/protos/tf_object_detection/hyperparams.proto',
  package='rastervision.protos.tf_object_detection',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n9rastervision/protos/tf_object_detection/hyperparams.proto\x12\'rastervision.protos.tf_object_detection\"\xfc\x03\n\x0bHyperparams\x12I\n\x02op\x18\x01 \x01(\x0e\x32\x37.rastervision.protos.tf_object_detection.Hyperparams.Op:\x04\x43ONV\x12I\n\x0bregularizer\x18\x02 \x01(\x0b\x32\x34.rastervision.protos.tf_object_detection.Regularizer\x12I\n\x0binitializer\x18\x03 \x01(\x0b\x32\x34.rastervision.protos.tf_object_detection.Initializer\x12Y\n\nactivation\x18\x04 \x01(\x0e\x32?.rastervision.protos.tf_object_detection.Hyperparams.Activation:\x04RELU\x12\x46\n\nbatch_norm\x18\x05 \x01(\x0b\x32\x32.rastervision.protos.tf_object_detection.BatchNorm\x12#\n\x14regularize_depthwise\x18\x06 \x01(\x08:\x05\x66\x61lse\"\x16\n\x02Op\x12\x08\n\x04\x43ONV\x10\x01\x12\x06\n\x02\x46\x43\x10\x02\",\n\nActivation\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04RELU\x10\x01\x12\n\n\x06RELU_6\x10\x02\"\xc6\x01\n\x0bRegularizer\x12P\n\x0el1_regularizer\x18\x01 \x01(\x0b\x32\x36.rastervision.protos.tf_object_detection.L1RegularizerH\x00\x12P\n\x0el2_regularizer\x18\x02 \x01(\x0b\x32\x36.rastervision.protos.tf_object_detection.L2RegularizerH\x00\x42\x13\n\x11regularizer_oneof\"\"\n\rL1Regularizer\x12\x11\n\x06weight\x18\x01 \x01(\x02:\x01\x31\"\"\n\rL2Regularizer\x12\x11\n\x06weight\x18\x01 \x01(\x02:\x01\x31\"\xe3\x02\n\x0bInitializer\x12k\n\x1ctruncated_normal_initializer\x18\x01 \x01(\x0b\x32\x43.rastervision.protos.tf_object_detection.TruncatedNormalInitializerH\x00\x12k\n\x1cvariance_scaling_initializer\x18\x02 \x01(\x0b\x32\x43.rastervision.protos.tf_object_detection.VarianceScalingInitializerH\x00\x12\x65\n\x19random_normal_initializer\x18\x03 \x01(\x0b\x32@.rastervision.protos.tf_object_detection.RandomNormalInitializerH\x00\x42\x13\n\x11initializer_oneof\"@\n\x1aTruncatedNormalInitializer\x12\x0f\n\x04mean\x18\x01 \x01(\x02:\x01\x30\x12\x11\n\x06stddev\x18\x02 \x01(\x02:\x01\x31\"\xd5\x01\n\x1aVarianceScalingInitializer\x12\x11\n\x06\x66\x61\x63tor\x18\x01 \x01(\x02:\x01\x32\x12\x16\n\x07uniform\x18\x02 \x01(\x08:\x05\x66\x61lse\x12^\n\x04mode\x18\x03 \x01(\x0e\x32H.rastervision.protos.tf_object_detection.VarianceScalingInitializer.Mode:\x06\x46\x41N_IN\",\n\x04Mode\x12\n\n\x06\x46\x41N_IN\x10\x00\x12\x0b\n\x07\x46\x41N_OUT\x10\x01\x12\x0b\n\x07\x46\x41N_AVG\x10\x02\"=\n\x17RandomNormalInitializer\x12\x0f\n\x04mean\x18\x01 \x01(\x02:\x01\x30\x12\x11\n\x06stddev\x18\x02 \x01(\x02:\x01\x31\"z\n\tBatchNorm\x12\x14\n\x05\x64\x65\x63\x61y\x18\x01 \x01(\x02:\x05\x30.999\x12\x14\n\x06\x63\x65nter\x18\x02 \x01(\x08:\x04true\x12\x14\n\x05scale\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x16\n\x07\x65psilon\x18\x04 \x01(\x02:\x05\x30.001\x12\x13\n\x05train\x18\x05 \x01(\x08:\x04true')
)



_HYPERPARAMS_OP = _descriptor.EnumDescriptor(
  name='Op',
  full_name='rastervision.protos.tf_object_detection.Hyperparams.Op',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONV', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FC', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=543,
  serialized_end=565,
)
_sym_db.RegisterEnumDescriptor(_HYPERPARAMS_OP)

_HYPERPARAMS_ACTIVATION = _descriptor.EnumDescriptor(
  name='Activation',
  full_name='rastervision.protos.tf_object_detection.Hyperparams.Activation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RELU', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RELU_6', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=567,
  serialized_end=611,
)
_sym_db.RegisterEnumDescriptor(_HYPERPARAMS_ACTIVATION)

_VARIANCESCALINGINITIALIZER_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='rastervision.protos.tf_object_detection.VarianceScalingInitializer.Mode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FAN_IN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAN_OUT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAN_AVG', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1480,
  serialized_end=1524,
)
_sym_db.RegisterEnumDescriptor(_VARIANCESCALINGINITIALIZER_MODE)


_HYPERPARAMS = _descriptor.Descriptor(
  name='Hyperparams',
  full_name='rastervision.protos.tf_object_detection.Hyperparams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='op', full_name='rastervision.protos.tf_object_detection.Hyperparams.op', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='regularizer', full_name='rastervision.protos.tf_object_detection.Hyperparams.regularizer', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initializer', full_name='rastervision.protos.tf_object_detection.Hyperparams.initializer', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activation', full_name='rastervision.protos.tf_object_detection.Hyperparams.activation', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch_norm', full_name='rastervision.protos.tf_object_detection.Hyperparams.batch_norm', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='regularize_depthwise', full_name='rastervision.protos.tf_object_detection.Hyperparams.regularize_depthwise', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HYPERPARAMS_OP,
    _HYPERPARAMS_ACTIVATION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=611,
)


_REGULARIZER = _descriptor.Descriptor(
  name='Regularizer',
  full_name='rastervision.protos.tf_object_detection.Regularizer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='l1_regularizer', full_name='rastervision.protos.tf_object_detection.Regularizer.l1_regularizer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='l2_regularizer', full_name='rastervision.protos.tf_object_detection.Regularizer.l2_regularizer', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='regularizer_oneof', full_name='rastervision.protos.tf_object_detection.Regularizer.regularizer_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=614,
  serialized_end=812,
)


_L1REGULARIZER = _descriptor.Descriptor(
  name='L1Regularizer',
  full_name='rastervision.protos.tf_object_detection.L1Regularizer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weight', full_name='rastervision.protos.tf_object_detection.L1Regularizer.weight', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
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
  serialized_start=814,
  serialized_end=848,
)


_L2REGULARIZER = _descriptor.Descriptor(
  name='L2Regularizer',
  full_name='rastervision.protos.tf_object_detection.L2Regularizer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weight', full_name='rastervision.protos.tf_object_detection.L2Regularizer.weight', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
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
  serialized_start=850,
  serialized_end=884,
)


_INITIALIZER = _descriptor.Descriptor(
  name='Initializer',
  full_name='rastervision.protos.tf_object_detection.Initializer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='truncated_normal_initializer', full_name='rastervision.protos.tf_object_detection.Initializer.truncated_normal_initializer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='variance_scaling_initializer', full_name='rastervision.protos.tf_object_detection.Initializer.variance_scaling_initializer', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='random_normal_initializer', full_name='rastervision.protos.tf_object_detection.Initializer.random_normal_initializer', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='initializer_oneof', full_name='rastervision.protos.tf_object_detection.Initializer.initializer_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=887,
  serialized_end=1242,
)


_TRUNCATEDNORMALINITIALIZER = _descriptor.Descriptor(
  name='TruncatedNormalInitializer',
  full_name='rastervision.protos.tf_object_detection.TruncatedNormalInitializer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mean', full_name='rastervision.protos.tf_object_detection.TruncatedNormalInitializer.mean', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stddev', full_name='rastervision.protos.tf_object_detection.TruncatedNormalInitializer.stddev', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
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
  serialized_start=1244,
  serialized_end=1308,
)


_VARIANCESCALINGINITIALIZER = _descriptor.Descriptor(
  name='VarianceScalingInitializer',
  full_name='rastervision.protos.tf_object_detection.VarianceScalingInitializer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='factor', full_name='rastervision.protos.tf_object_detection.VarianceScalingInitializer.factor', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(2),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uniform', full_name='rastervision.protos.tf_object_detection.VarianceScalingInitializer.uniform', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='rastervision.protos.tf_object_detection.VarianceScalingInitializer.mode', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VARIANCESCALINGINITIALIZER_MODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1311,
  serialized_end=1524,
)


_RANDOMNORMALINITIALIZER = _descriptor.Descriptor(
  name='RandomNormalInitializer',
  full_name='rastervision.protos.tf_object_detection.RandomNormalInitializer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mean', full_name='rastervision.protos.tf_object_detection.RandomNormalInitializer.mean', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stddev', full_name='rastervision.protos.tf_object_detection.RandomNormalInitializer.stddev', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
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
  serialized_start=1526,
  serialized_end=1587,
)


_BATCHNORM = _descriptor.Descriptor(
  name='BatchNorm',
  full_name='rastervision.protos.tf_object_detection.BatchNorm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='decay', full_name='rastervision.protos.tf_object_detection.BatchNorm.decay', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.999),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='center', full_name='rastervision.protos.tf_object_detection.BatchNorm.center', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale', full_name='rastervision.protos.tf_object_detection.BatchNorm.scale', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='epsilon', full_name='rastervision.protos.tf_object_detection.BatchNorm.epsilon', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.001),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='train', full_name='rastervision.protos.tf_object_detection.BatchNorm.train', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
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
  serialized_start=1589,
  serialized_end=1711,
)

_HYPERPARAMS.fields_by_name['op'].enum_type = _HYPERPARAMS_OP
_HYPERPARAMS.fields_by_name['regularizer'].message_type = _REGULARIZER
_HYPERPARAMS.fields_by_name['initializer'].message_type = _INITIALIZER
_HYPERPARAMS.fields_by_name['activation'].enum_type = _HYPERPARAMS_ACTIVATION
_HYPERPARAMS.fields_by_name['batch_norm'].message_type = _BATCHNORM
_HYPERPARAMS_OP.containing_type = _HYPERPARAMS
_HYPERPARAMS_ACTIVATION.containing_type = _HYPERPARAMS
_REGULARIZER.fields_by_name['l1_regularizer'].message_type = _L1REGULARIZER
_REGULARIZER.fields_by_name['l2_regularizer'].message_type = _L2REGULARIZER
_REGULARIZER.oneofs_by_name['regularizer_oneof'].fields.append(
  _REGULARIZER.fields_by_name['l1_regularizer'])
_REGULARIZER.fields_by_name['l1_regularizer'].containing_oneof = _REGULARIZER.oneofs_by_name['regularizer_oneof']
_REGULARIZER.oneofs_by_name['regularizer_oneof'].fields.append(
  _REGULARIZER.fields_by_name['l2_regularizer'])
_REGULARIZER.fields_by_name['l2_regularizer'].containing_oneof = _REGULARIZER.oneofs_by_name['regularizer_oneof']
_INITIALIZER.fields_by_name['truncated_normal_initializer'].message_type = _TRUNCATEDNORMALINITIALIZER
_INITIALIZER.fields_by_name['variance_scaling_initializer'].message_type = _VARIANCESCALINGINITIALIZER
_INITIALIZER.fields_by_name['random_normal_initializer'].message_type = _RANDOMNORMALINITIALIZER
_INITIALIZER.oneofs_by_name['initializer_oneof'].fields.append(
  _INITIALIZER.fields_by_name['truncated_normal_initializer'])
_INITIALIZER.fields_by_name['truncated_normal_initializer'].containing_oneof = _INITIALIZER.oneofs_by_name['initializer_oneof']
_INITIALIZER.oneofs_by_name['initializer_oneof'].fields.append(
  _INITIALIZER.fields_by_name['variance_scaling_initializer'])
_INITIALIZER.fields_by_name['variance_scaling_initializer'].containing_oneof = _INITIALIZER.oneofs_by_name['initializer_oneof']
_INITIALIZER.oneofs_by_name['initializer_oneof'].fields.append(
  _INITIALIZER.fields_by_name['random_normal_initializer'])
_INITIALIZER.fields_by_name['random_normal_initializer'].containing_oneof = _INITIALIZER.oneofs_by_name['initializer_oneof']
_VARIANCESCALINGINITIALIZER.fields_by_name['mode'].enum_type = _VARIANCESCALINGINITIALIZER_MODE
_VARIANCESCALINGINITIALIZER_MODE.containing_type = _VARIANCESCALINGINITIALIZER
DESCRIPTOR.message_types_by_name['Hyperparams'] = _HYPERPARAMS
DESCRIPTOR.message_types_by_name['Regularizer'] = _REGULARIZER
DESCRIPTOR.message_types_by_name['L1Regularizer'] = _L1REGULARIZER
DESCRIPTOR.message_types_by_name['L2Regularizer'] = _L2REGULARIZER
DESCRIPTOR.message_types_by_name['Initializer'] = _INITIALIZER
DESCRIPTOR.message_types_by_name['TruncatedNormalInitializer'] = _TRUNCATEDNORMALINITIALIZER
DESCRIPTOR.message_types_by_name['VarianceScalingInitializer'] = _VARIANCESCALINGINITIALIZER
DESCRIPTOR.message_types_by_name['RandomNormalInitializer'] = _RANDOMNORMALINITIALIZER
DESCRIPTOR.message_types_by_name['BatchNorm'] = _BATCHNORM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Hyperparams = _reflection.GeneratedProtocolMessageType('Hyperparams', (_message.Message,), dict(
  DESCRIPTOR = _HYPERPARAMS,
  __module__ = 'rastervision.protos.tf_object_detection.hyperparams_pb2'
  # @@protoc_insertion_point(class_scope:rastervision.protos.tf_object_detection.Hyperparams)
  ))
_sym_db.RegisterMessage(Hyperparams)

Regularizer = _reflection.GeneratedProtocolMessageType('Regularizer', (_message.Message,), dict(
  DESCRIPTOR = _REGULARIZER,
  __module__ = 'rastervision.protos.tf_object_detection.hyperparams_pb2'
  # @@protoc_insertion_point(class_scope:rastervision.protos.tf_object_detection.Regularizer)
  ))
_sym_db.RegisterMessage(Regularizer)

L1Regularizer = _reflection.GeneratedProtocolMessageType('L1Regularizer', (_message.Message,), dict(
  DESCRIPTOR = _L1REGULARIZER,
  __module__ = 'rastervision.protos.tf_object_detection.hyperparams_pb2'
  # @@protoc_insertion_point(class_scope:rastervision.protos.tf_object_detection.L1Regularizer)
  ))
_sym_db.RegisterMessage(L1Regularizer)

L2Regularizer = _reflection.GeneratedProtocolMessageType('L2Regularizer', (_message.Message,), dict(
  DESCRIPTOR = _L2REGULARIZER,
  __module__ = 'rastervision.protos.tf_object_detection.hyperparams_pb2'
  # @@protoc_insertion_point(class_scope:rastervision.protos.tf_object_detection.L2Regularizer)
  ))
_sym_db.RegisterMessage(L2Regularizer)

Initializer = _reflection.GeneratedProtocolMessageType('Initializer', (_message.Message,), dict(
  DESCRIPTOR = _INITIALIZER,
  __module__ = 'rastervision.protos.tf_object_detection.hyperparams_pb2'
  # @@protoc_insertion_point(class_scope:rastervision.protos.tf_object_detection.Initializer)
  ))
_sym_db.RegisterMessage(Initializer)

TruncatedNormalInitializer = _reflection.GeneratedProtocolMessageType('TruncatedNormalInitializer', (_message.Message,), dict(
  DESCRIPTOR = _TRUNCATEDNORMALINITIALIZER,
  __module__ = 'rastervision.protos.tf_object_detection.hyperparams_pb2'
  # @@protoc_insertion_point(class_scope:rastervision.protos.tf_object_detection.TruncatedNormalInitializer)
  ))
_sym_db.RegisterMessage(TruncatedNormalInitializer)

VarianceScalingInitializer = _reflection.GeneratedProtocolMessageType('VarianceScalingInitializer', (_message.Message,), dict(
  DESCRIPTOR = _VARIANCESCALINGINITIALIZER,
  __module__ = 'rastervision.protos.tf_object_detection.hyperparams_pb2'
  # @@protoc_insertion_point(class_scope:rastervision.protos.tf_object_detection.VarianceScalingInitializer)
  ))
_sym_db.RegisterMessage(VarianceScalingInitializer)

RandomNormalInitializer = _reflection.GeneratedProtocolMessageType('RandomNormalInitializer', (_message.Message,), dict(
  DESCRIPTOR = _RANDOMNORMALINITIALIZER,
  __module__ = 'rastervision.protos.tf_object_detection.hyperparams_pb2'
  # @@protoc_insertion_point(class_scope:rastervision.protos.tf_object_detection.RandomNormalInitializer)
  ))
_sym_db.RegisterMessage(RandomNormalInitializer)

BatchNorm = _reflection.GeneratedProtocolMessageType('BatchNorm', (_message.Message,), dict(
  DESCRIPTOR = _BATCHNORM,
  __module__ = 'rastervision.protos.tf_object_detection.hyperparams_pb2'
  # @@protoc_insertion_point(class_scope:rastervision.protos.tf_object_detection.BatchNorm)
  ))
_sym_db.RegisterMessage(BatchNorm)


# @@protoc_insertion_point(module_scope)
