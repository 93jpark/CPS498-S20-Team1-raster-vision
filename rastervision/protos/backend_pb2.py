# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rastervision/protos/backend.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rastervision/protos/backend.proto',
  package='rv.protos',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n!rastervision/protos/backend.proto\x12\trv.protos\x1a\x1cgoogle/protobuf/struct.proto\"\xab\x0c\n\rBackendConfig\x12\x14\n\x0c\x62\x61\x63kend_type\x18\x01 \x02(\t\x12\x1c\n\x14pretrained_model_uri\x18\x03 \x01(\t\x12V\n\x1atf_object_detection_config\x18\x04 \x01(\x0b\x32\x30.rv.protos.BackendConfig.TFObjectDetectionConfigH\x00\x12Y\n\x1bkeras_classification_config\x18\x05 \x01(\x0b\x32\x32.rv.protos.BackendConfig.KerasClassificationConfigH\x00\x12\x45\n\x11tf_deeplab_config\x18\x07 \x01(\x0b\x32(.rv.protos.BackendConfig.TFDeeplabConfigH\x00\x12\x30\n\rcustom_config\x18\x06 \x01(\x0b\x32\x17.google.protobuf.StructH\x00\x1a\xb6\x03\n\x17TFObjectDetectionConfig\x12\x1a\n\rsync_interval\x18\x01 \x01(\x05:\x03\x36\x30\x30\x12\x1b\n\rdo_monitoring\x18\x02 \x01(\x08:\x04true\x12\x1c\n\rreplace_model\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x44\n\rmodel_main_py\x18\x04 \x01(\t:-/opt/tf-models/object_detection/model_main.py\x12L\n\texport_py\x18\x05 \x01(\t:9/opt/tf-models/object_detection/export_inference_graph.py\x12\x19\n\x11training_data_uri\x18\x06 \x01(\t\x12\x1b\n\x13training_output_uri\x18\x07 \x01(\t\x12\x11\n\tmodel_uri\x18\x08 \x01(\t\x12!\n\x19\x66ine_tune_checkpoint_name\x18\t \x01(\t\x12\x14\n\x05\x64\x65\x62ug\x18\n \x01(\x08:\x05\x66\x61lse\x12,\n\x0btfod_config\x18\x0b \x02(\x0b\x32\x17.google.protobuf.Struct\x1a\xff\x01\n\x19KerasClassificationConfig\x12\x1a\n\rsync_interval\x18\x01 \x01(\x05:\x03\x36\x30\x30\x12\x1b\n\rdo_monitoring\x18\x02 \x01(\x08:\x04true\x12\x1c\n\rreplace_model\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x19\n\x11training_data_uri\x18\x04 \x01(\t\x12\x1b\n\x13training_output_uri\x18\x05 \x01(\t\x12\x11\n\tmodel_uri\x18\x06 \x01(\t\x12\x14\n\x05\x64\x65\x62ug\x18\x07 \x01(\x08:\x05\x66\x61lse\x12*\n\tkc_config\x18\x08 \x02(\x0b\x32\x17.google.protobuf.Struct\x1a\xec\x03\n\x0fTFDeeplabConfig\x12\x31\n\x08train_py\x18\x01 \x01(\t:\x1f/opt/tf-models/deeplab/train.py\x12/\n\x07\x65val_py\x18\x0e \x01(\t:\x1e/opt/tf-models/deeplab/eval.py\x12\x39\n\texport_py\x18\x02 \x01(\t:&/opt/tf-models/deeplab/export_model.py\x12\x19\n\x11train_restart_dir\x18\x03 \x01(\t\x12\x1a\n\rsync_interval\x18\x04 \x01(\x05:\x03\x36\x30\x30\x12\x1b\n\rdo_monitoring\x18\x05 \x01(\x08:\x04true\x12\x16\n\x07\x64o_eval\x18\r \x01(\x08:\x05\x66\x61lse\x12\x1c\n\rreplace_model\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x19\n\x11training_data_uri\x18\x07 \x01(\t\x12\x1b\n\x13training_output_uri\x18\x08 \x01(\t\x12\x11\n\tmodel_uri\x18\t \x01(\t\x12!\n\x19\x66ine_tune_checkpoint_name\x18\n \x01(\t\x12,\n\x0btfdl_config\x18\x0b \x02(\x0b\x32\x17.google.protobuf.Struct\x12\x14\n\x05\x64\x65\x62ug\x18\x0c \x01(\x08:\x05\x66\x61lseB\x10\n\x0e\x62\x61\x63kend_config')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_BACKENDCONFIG_TFOBJECTDETECTIONCONFIG = _descriptor.Descriptor(
  name='TFObjectDetectionConfig',
  full_name='rv.protos.BackendConfig.TFObjectDetectionConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sync_interval', full_name='rv.protos.BackendConfig.TFObjectDetectionConfig.sync_interval', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=600,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='do_monitoring', full_name='rv.protos.BackendConfig.TFObjectDetectionConfig.do_monitoring', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='replace_model', full_name='rv.protos.BackendConfig.TFObjectDetectionConfig.replace_model', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_main_py', full_name='rv.protos.BackendConfig.TFObjectDetectionConfig.model_main_py', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("/opt/tf-models/object_detection/model_main.py").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='export_py', full_name='rv.protos.BackendConfig.TFObjectDetectionConfig.export_py', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("/opt/tf-models/object_detection/export_inference_graph.py").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='training_data_uri', full_name='rv.protos.BackendConfig.TFObjectDetectionConfig.training_data_uri', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='training_output_uri', full_name='rv.protos.BackendConfig.TFObjectDetectionConfig.training_output_uri', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_uri', full_name='rv.protos.BackendConfig.TFObjectDetectionConfig.model_uri', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fine_tune_checkpoint_name', full_name='rv.protos.BackendConfig.TFObjectDetectionConfig.fine_tune_checkpoint_name', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='debug', full_name='rv.protos.BackendConfig.TFObjectDetectionConfig.debug', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tfod_config', full_name='rv.protos.BackendConfig.TFObjectDetectionConfig.tfod_config', index=10,
      number=11, type=11, cpp_type=10, label=2,
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
  serialized_start=449,
  serialized_end=887,
)

_BACKENDCONFIG_KERASCLASSIFICATIONCONFIG = _descriptor.Descriptor(
  name='KerasClassificationConfig',
  full_name='rv.protos.BackendConfig.KerasClassificationConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sync_interval', full_name='rv.protos.BackendConfig.KerasClassificationConfig.sync_interval', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=600,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='do_monitoring', full_name='rv.protos.BackendConfig.KerasClassificationConfig.do_monitoring', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='replace_model', full_name='rv.protos.BackendConfig.KerasClassificationConfig.replace_model', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='training_data_uri', full_name='rv.protos.BackendConfig.KerasClassificationConfig.training_data_uri', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='training_output_uri', full_name='rv.protos.BackendConfig.KerasClassificationConfig.training_output_uri', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_uri', full_name='rv.protos.BackendConfig.KerasClassificationConfig.model_uri', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='debug', full_name='rv.protos.BackendConfig.KerasClassificationConfig.debug', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kc_config', full_name='rv.protos.BackendConfig.KerasClassificationConfig.kc_config', index=7,
      number=8, type=11, cpp_type=10, label=2,
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
  serialized_start=890,
  serialized_end=1145,
)

_BACKENDCONFIG_TFDEEPLABCONFIG = _descriptor.Descriptor(
  name='TFDeeplabConfig',
  full_name='rv.protos.BackendConfig.TFDeeplabConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='train_py', full_name='rv.protos.BackendConfig.TFDeeplabConfig.train_py', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("/opt/tf-models/deeplab/train.py").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eval_py', full_name='rv.protos.BackendConfig.TFDeeplabConfig.eval_py', index=1,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("/opt/tf-models/deeplab/eval.py").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='export_py', full_name='rv.protos.BackendConfig.TFDeeplabConfig.export_py', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("/opt/tf-models/deeplab/export_model.py").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='train_restart_dir', full_name='rv.protos.BackendConfig.TFDeeplabConfig.train_restart_dir', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sync_interval', full_name='rv.protos.BackendConfig.TFDeeplabConfig.sync_interval', index=4,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=600,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='do_monitoring', full_name='rv.protos.BackendConfig.TFDeeplabConfig.do_monitoring', index=5,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='do_eval', full_name='rv.protos.BackendConfig.TFDeeplabConfig.do_eval', index=6,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='replace_model', full_name='rv.protos.BackendConfig.TFDeeplabConfig.replace_model', index=7,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='training_data_uri', full_name='rv.protos.BackendConfig.TFDeeplabConfig.training_data_uri', index=8,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='training_output_uri', full_name='rv.protos.BackendConfig.TFDeeplabConfig.training_output_uri', index=9,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_uri', full_name='rv.protos.BackendConfig.TFDeeplabConfig.model_uri', index=10,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fine_tune_checkpoint_name', full_name='rv.protos.BackendConfig.TFDeeplabConfig.fine_tune_checkpoint_name', index=11,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tfdl_config', full_name='rv.protos.BackendConfig.TFDeeplabConfig.tfdl_config', index=12,
      number=11, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='debug', full_name='rv.protos.BackendConfig.TFDeeplabConfig.debug', index=13,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  serialized_start=1148,
  serialized_end=1640,
)

_BACKENDCONFIG = _descriptor.Descriptor(
  name='BackendConfig',
  full_name='rv.protos.BackendConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='backend_type', full_name='rv.protos.BackendConfig.backend_type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pretrained_model_uri', full_name='rv.protos.BackendConfig.pretrained_model_uri', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tf_object_detection_config', full_name='rv.protos.BackendConfig.tf_object_detection_config', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keras_classification_config', full_name='rv.protos.BackendConfig.keras_classification_config', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tf_deeplab_config', full_name='rv.protos.BackendConfig.tf_deeplab_config', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='custom_config', full_name='rv.protos.BackendConfig.custom_config', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BACKENDCONFIG_TFOBJECTDETECTIONCONFIG, _BACKENDCONFIG_KERASCLASSIFICATIONCONFIG, _BACKENDCONFIG_TFDEEPLABCONFIG, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='backend_config', full_name='rv.protos.BackendConfig.backend_config',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=79,
  serialized_end=1658,
)

_BACKENDCONFIG_TFOBJECTDETECTIONCONFIG.fields_by_name['tfod_config'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_BACKENDCONFIG_TFOBJECTDETECTIONCONFIG.containing_type = _BACKENDCONFIG
_BACKENDCONFIG_KERASCLASSIFICATIONCONFIG.fields_by_name['kc_config'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_BACKENDCONFIG_KERASCLASSIFICATIONCONFIG.containing_type = _BACKENDCONFIG
_BACKENDCONFIG_TFDEEPLABCONFIG.fields_by_name['tfdl_config'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_BACKENDCONFIG_TFDEEPLABCONFIG.containing_type = _BACKENDCONFIG
_BACKENDCONFIG.fields_by_name['tf_object_detection_config'].message_type = _BACKENDCONFIG_TFOBJECTDETECTIONCONFIG
_BACKENDCONFIG.fields_by_name['keras_classification_config'].message_type = _BACKENDCONFIG_KERASCLASSIFICATIONCONFIG
_BACKENDCONFIG.fields_by_name['tf_deeplab_config'].message_type = _BACKENDCONFIG_TFDEEPLABCONFIG
_BACKENDCONFIG.fields_by_name['custom_config'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_BACKENDCONFIG.oneofs_by_name['backend_config'].fields.append(
  _BACKENDCONFIG.fields_by_name['tf_object_detection_config'])
_BACKENDCONFIG.fields_by_name['tf_object_detection_config'].containing_oneof = _BACKENDCONFIG.oneofs_by_name['backend_config']
_BACKENDCONFIG.oneofs_by_name['backend_config'].fields.append(
  _BACKENDCONFIG.fields_by_name['keras_classification_config'])
_BACKENDCONFIG.fields_by_name['keras_classification_config'].containing_oneof = _BACKENDCONFIG.oneofs_by_name['backend_config']
_BACKENDCONFIG.oneofs_by_name['backend_config'].fields.append(
  _BACKENDCONFIG.fields_by_name['tf_deeplab_config'])
_BACKENDCONFIG.fields_by_name['tf_deeplab_config'].containing_oneof = _BACKENDCONFIG.oneofs_by_name['backend_config']
_BACKENDCONFIG.oneofs_by_name['backend_config'].fields.append(
  _BACKENDCONFIG.fields_by_name['custom_config'])
_BACKENDCONFIG.fields_by_name['custom_config'].containing_oneof = _BACKENDCONFIG.oneofs_by_name['backend_config']
DESCRIPTOR.message_types_by_name['BackendConfig'] = _BACKENDCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BackendConfig = _reflection.GeneratedProtocolMessageType('BackendConfig', (_message.Message,), dict(

  TFObjectDetectionConfig = _reflection.GeneratedProtocolMessageType('TFObjectDetectionConfig', (_message.Message,), dict(
    DESCRIPTOR = _BACKENDCONFIG_TFOBJECTDETECTIONCONFIG,
    __module__ = 'rastervision.protos.backend_pb2'
    # @@protoc_insertion_point(class_scope:rv.protos.BackendConfig.TFObjectDetectionConfig)
    ))
  ,

  KerasClassificationConfig = _reflection.GeneratedProtocolMessageType('KerasClassificationConfig', (_message.Message,), dict(
    DESCRIPTOR = _BACKENDCONFIG_KERASCLASSIFICATIONCONFIG,
    __module__ = 'rastervision.protos.backend_pb2'
    # @@protoc_insertion_point(class_scope:rv.protos.BackendConfig.KerasClassificationConfig)
    ))
  ,

  TFDeeplabConfig = _reflection.GeneratedProtocolMessageType('TFDeeplabConfig', (_message.Message,), dict(
    DESCRIPTOR = _BACKENDCONFIG_TFDEEPLABCONFIG,
    __module__ = 'rastervision.protos.backend_pb2'
    # @@protoc_insertion_point(class_scope:rv.protos.BackendConfig.TFDeeplabConfig)
    ))
  ,
  DESCRIPTOR = _BACKENDCONFIG,
  __module__ = 'rastervision.protos.backend_pb2'
  # @@protoc_insertion_point(class_scope:rv.protos.BackendConfig)
  ))
_sym_db.RegisterMessage(BackendConfig)
_sym_db.RegisterMessage(BackendConfig.TFObjectDetectionConfig)
_sym_db.RegisterMessage(BackendConfig.KerasClassificationConfig)
_sym_db.RegisterMessage(BackendConfig.TFDeeplabConfig)


# @@protoc_insertion_point(module_scope)
