# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hfc/protos/orderer/ab.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from hfc.protos.common import common_pb2 as hfc_dot_protos_dot_common_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hfc/protos/orderer/ab.proto',
  package='orderer',
  syntax='proto3',
  serialized_options=_b('\n%org.hyperledger.fabric.protos.ordererZ,github.com/hyperledger/fabric/protos/orderer'),
  serialized_pb=_b('\n\x1bhfc/protos/orderer/ab.proto\x12\x07orderer\x1a\x1ehfc/protos/common/common.proto\"A\n\x11\x42roadcastResponse\x12\x1e\n\x06status\x18\x01 \x01(\x0e\x32\x0e.common.Status\x12\x0c\n\x04info\x18\x02 \x01(\t\"\x0c\n\nSeekNewest\"\x0c\n\nSeekOldest\"\x1f\n\rSeekSpecified\x12\x0e\n\x06number\x18\x01 \x01(\x04\"\x91\x01\n\x0cSeekPosition\x12%\n\x06newest\x18\x01 \x01(\x0b\x32\x13.orderer.SeekNewestH\x00\x12%\n\x06oldest\x18\x02 \x01(\x0b\x32\x13.orderer.SeekOldestH\x00\x12+\n\tspecified\x18\x03 \x01(\x0b\x32\x16.orderer.SeekSpecifiedH\x00\x42\x06\n\x04Type\"\xc5\x01\n\x08SeekInfo\x12$\n\x05start\x18\x01 \x01(\x0b\x32\x15.orderer.SeekPosition\x12#\n\x04stop\x18\x02 \x01(\x0b\x32\x15.orderer.SeekPosition\x12\x30\n\x08\x62\x65havior\x18\x03 \x01(\x0e\x32\x1e.orderer.SeekInfo.SeekBehavior\"<\n\x0cSeekBehavior\x12\x15\n\x11\x42LOCK_UNTIL_READY\x10\x00\x12\x15\n\x11\x46\x41IL_IF_NOT_READY\x10\x01\"[\n\x0f\x44\x65liverResponse\x12 \n\x06status\x18\x01 \x01(\x0e\x32\x0e.common.StatusH\x00\x12\x1e\n\x05\x62lock\x18\x02 \x01(\x0b\x32\r.common.BlockH\x00\x42\x06\n\x04Type2\x8f\x01\n\x0f\x41tomicBroadcast\x12?\n\tBroadcast\x12\x10.common.Envelope\x1a\x1a.orderer.BroadcastResponse\"\x00(\x01\x30\x01\x12;\n\x07\x44\x65liver\x12\x10.common.Envelope\x1a\x18.orderer.DeliverResponse\"\x00(\x01\x30\x01\x42U\n%org.hyperledger.fabric.protos.ordererZ,github.com/hyperledger/fabric/protos/ordererb\x06proto3')
  ,
  dependencies=[hfc_dot_protos_dot_common_dot_common__pb2.DESCRIPTOR,])



_SEEKINFO_SEEKBEHAVIOR = _descriptor.EnumDescriptor(
  name='SeekBehavior',
  full_name='orderer.SeekInfo.SeekBehavior',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BLOCK_UNTIL_READY', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAIL_IF_NOT_READY', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=486,
  serialized_end=546,
)
_sym_db.RegisterEnumDescriptor(_SEEKINFO_SEEKBEHAVIOR)


_BROADCASTRESPONSE = _descriptor.Descriptor(
  name='BroadcastResponse',
  full_name='orderer.BroadcastResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='orderer.BroadcastResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='orderer.BroadcastResponse.info', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=137,
)


_SEEKNEWEST = _descriptor.Descriptor(
  name='SeekNewest',
  full_name='orderer.SeekNewest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=139,
  serialized_end=151,
)


_SEEKOLDEST = _descriptor.Descriptor(
  name='SeekOldest',
  full_name='orderer.SeekOldest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=153,
  serialized_end=165,
)


_SEEKSPECIFIED = _descriptor.Descriptor(
  name='SeekSpecified',
  full_name='orderer.SeekSpecified',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='orderer.SeekSpecified.number', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=167,
  serialized_end=198,
)


_SEEKPOSITION = _descriptor.Descriptor(
  name='SeekPosition',
  full_name='orderer.SeekPosition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='newest', full_name='orderer.SeekPosition.newest', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oldest', full_name='orderer.SeekPosition.oldest', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='specified', full_name='orderer.SeekPosition.specified', index=2,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Type', full_name='orderer.SeekPosition.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=201,
  serialized_end=346,
)


_SEEKINFO = _descriptor.Descriptor(
  name='SeekInfo',
  full_name='orderer.SeekInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='orderer.SeekInfo.start', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='orderer.SeekInfo.stop', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='behavior', full_name='orderer.SeekInfo.behavior', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SEEKINFO_SEEKBEHAVIOR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=349,
  serialized_end=546,
)


_DELIVERRESPONSE = _descriptor.Descriptor(
  name='DeliverResponse',
  full_name='orderer.DeliverResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='orderer.DeliverResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block', full_name='orderer.DeliverResponse.block', index=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Type', full_name='orderer.DeliverResponse.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=548,
  serialized_end=639,
)

_BROADCASTRESPONSE.fields_by_name['status'].enum_type = hfc_dot_protos_dot_common_dot_common__pb2._STATUS
_SEEKPOSITION.fields_by_name['newest'].message_type = _SEEKNEWEST
_SEEKPOSITION.fields_by_name['oldest'].message_type = _SEEKOLDEST
_SEEKPOSITION.fields_by_name['specified'].message_type = _SEEKSPECIFIED
_SEEKPOSITION.oneofs_by_name['Type'].fields.append(
  _SEEKPOSITION.fields_by_name['newest'])
_SEEKPOSITION.fields_by_name['newest'].containing_oneof = _SEEKPOSITION.oneofs_by_name['Type']
_SEEKPOSITION.oneofs_by_name['Type'].fields.append(
  _SEEKPOSITION.fields_by_name['oldest'])
_SEEKPOSITION.fields_by_name['oldest'].containing_oneof = _SEEKPOSITION.oneofs_by_name['Type']
_SEEKPOSITION.oneofs_by_name['Type'].fields.append(
  _SEEKPOSITION.fields_by_name['specified'])
_SEEKPOSITION.fields_by_name['specified'].containing_oneof = _SEEKPOSITION.oneofs_by_name['Type']
_SEEKINFO.fields_by_name['start'].message_type = _SEEKPOSITION
_SEEKINFO.fields_by_name['stop'].message_type = _SEEKPOSITION
_SEEKINFO.fields_by_name['behavior'].enum_type = _SEEKINFO_SEEKBEHAVIOR
_SEEKINFO_SEEKBEHAVIOR.containing_type = _SEEKINFO
_DELIVERRESPONSE.fields_by_name['status'].enum_type = hfc_dot_protos_dot_common_dot_common__pb2._STATUS
_DELIVERRESPONSE.fields_by_name['block'].message_type = hfc_dot_protos_dot_common_dot_common__pb2._BLOCK
_DELIVERRESPONSE.oneofs_by_name['Type'].fields.append(
  _DELIVERRESPONSE.fields_by_name['status'])
_DELIVERRESPONSE.fields_by_name['status'].containing_oneof = _DELIVERRESPONSE.oneofs_by_name['Type']
_DELIVERRESPONSE.oneofs_by_name['Type'].fields.append(
  _DELIVERRESPONSE.fields_by_name['block'])
_DELIVERRESPONSE.fields_by_name['block'].containing_oneof = _DELIVERRESPONSE.oneofs_by_name['Type']
DESCRIPTOR.message_types_by_name['BroadcastResponse'] = _BROADCASTRESPONSE
DESCRIPTOR.message_types_by_name['SeekNewest'] = _SEEKNEWEST
DESCRIPTOR.message_types_by_name['SeekOldest'] = _SEEKOLDEST
DESCRIPTOR.message_types_by_name['SeekSpecified'] = _SEEKSPECIFIED
DESCRIPTOR.message_types_by_name['SeekPosition'] = _SEEKPOSITION
DESCRIPTOR.message_types_by_name['SeekInfo'] = _SEEKINFO
DESCRIPTOR.message_types_by_name['DeliverResponse'] = _DELIVERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BroadcastResponse = _reflection.GeneratedProtocolMessageType('BroadcastResponse', (_message.Message,), dict(
  DESCRIPTOR = _BROADCASTRESPONSE,
  __module__ = 'hfc.protos.orderer.ab_pb2'
  # @@protoc_insertion_point(class_scope:orderer.BroadcastResponse)
  ))
_sym_db.RegisterMessage(BroadcastResponse)

SeekNewest = _reflection.GeneratedProtocolMessageType('SeekNewest', (_message.Message,), dict(
  DESCRIPTOR = _SEEKNEWEST,
  __module__ = 'hfc.protos.orderer.ab_pb2'
  # @@protoc_insertion_point(class_scope:orderer.SeekNewest)
  ))
_sym_db.RegisterMessage(SeekNewest)

SeekOldest = _reflection.GeneratedProtocolMessageType('SeekOldest', (_message.Message,), dict(
  DESCRIPTOR = _SEEKOLDEST,
  __module__ = 'hfc.protos.orderer.ab_pb2'
  # @@protoc_insertion_point(class_scope:orderer.SeekOldest)
  ))
_sym_db.RegisterMessage(SeekOldest)

SeekSpecified = _reflection.GeneratedProtocolMessageType('SeekSpecified', (_message.Message,), dict(
  DESCRIPTOR = _SEEKSPECIFIED,
  __module__ = 'hfc.protos.orderer.ab_pb2'
  # @@protoc_insertion_point(class_scope:orderer.SeekSpecified)
  ))
_sym_db.RegisterMessage(SeekSpecified)

SeekPosition = _reflection.GeneratedProtocolMessageType('SeekPosition', (_message.Message,), dict(
  DESCRIPTOR = _SEEKPOSITION,
  __module__ = 'hfc.protos.orderer.ab_pb2'
  # @@protoc_insertion_point(class_scope:orderer.SeekPosition)
  ))
_sym_db.RegisterMessage(SeekPosition)

SeekInfo = _reflection.GeneratedProtocolMessageType('SeekInfo', (_message.Message,), dict(
  DESCRIPTOR = _SEEKINFO,
  __module__ = 'hfc.protos.orderer.ab_pb2'
  # @@protoc_insertion_point(class_scope:orderer.SeekInfo)
  ))
_sym_db.RegisterMessage(SeekInfo)

DeliverResponse = _reflection.GeneratedProtocolMessageType('DeliverResponse', (_message.Message,), dict(
  DESCRIPTOR = _DELIVERRESPONSE,
  __module__ = 'hfc.protos.orderer.ab_pb2'
  # @@protoc_insertion_point(class_scope:orderer.DeliverResponse)
  ))
_sym_db.RegisterMessage(DeliverResponse)


DESCRIPTOR._options = None

_ATOMICBROADCAST = _descriptor.ServiceDescriptor(
  name='AtomicBroadcast',
  full_name='orderer.AtomicBroadcast',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=642,
  serialized_end=785,
  methods=[
  _descriptor.MethodDescriptor(
    name='Broadcast',
    full_name='orderer.AtomicBroadcast.Broadcast',
    index=0,
    containing_service=None,
    input_type=hfc_dot_protos_dot_common_dot_common__pb2._ENVELOPE,
    output_type=_BROADCASTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Deliver',
    full_name='orderer.AtomicBroadcast.Deliver',
    index=1,
    containing_service=None,
    input_type=hfc_dot_protos_dot_common_dot_common__pb2._ENVELOPE,
    output_type=_DELIVERRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ATOMICBROADCAST)

DESCRIPTOR.services_by_name['AtomicBroadcast'] = _ATOMICBROADCAST

# @@protoc_insertion_point(module_scope)
