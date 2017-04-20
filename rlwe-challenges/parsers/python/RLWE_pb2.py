# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RLWE.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Lol_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='RLWE.proto',
  package='crypto.proto.RLWE',
  serialized_pb=_b('\n\nRLWE.proto\x12\x11\x63rypto.proto.RLWE\x1a\tLol.proto\"N\n\nSampleCont\x12\x1f\n\x01\x61\x18\x01 \x02(\x0b\x32\x14.crypto.proto.lol.Rq\x12\x1f\n\x01\x62\x18\x02 \x02(\x0b\x32\x14.crypto.proto.lol.Kq\"N\n\nSampleDisc\x12\x1f\n\x01\x61\x18\x01 \x02(\x0b\x32\x14.crypto.proto.lol.Rq\x12\x1f\n\x01\x62\x18\x02 \x02(\x0b\x32\x14.crypto.proto.lol.Rq\"N\n\nSampleRLWR\x12\x1f\n\x01\x61\x18\x01 \x02(\x0b\x32\x14.crypto.proto.lol.Rq\x12\x1f\n\x01\x62\x18\x02 \x02(\x0b\x32\x14.crypto.proto.lol.Rq\"c\n\x11SampleContProduct\x12&\n\x01\x61\x18\x01 \x02(\x0b\x32\x1b.crypto.proto.lol.RqProduct\x12&\n\x01\x62\x18\x02 \x02(\x0b\x32\x1b.crypto.proto.lol.KqProduct\"c\n\x11SampleDiscProduct\x12&\n\x01\x61\x18\x01 \x02(\x0b\x32\x1b.crypto.proto.lol.RqProduct\x12&\n\x01\x62\x18\x02 \x02(\x0b\x32\x1b.crypto.proto.lol.RqProduct\"c\n\x11SampleRLWRProduct\x12&\n\x01\x61\x18\x01 \x02(\x0b\x32\x1b.crypto.proto.lol.RqProduct\x12&\n\x01\x62\x18\x02 \x02(\x0b\x32\x1b.crypto.proto.lol.RqProduct')
  ,
  dependencies=[Lol_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SAMPLECONT = _descriptor.Descriptor(
  name='SampleCont',
  full_name='crypto.proto.RLWE.SampleCont',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='crypto.proto.RLWE.SampleCont.a', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='b', full_name='crypto.proto.RLWE.SampleCont.b', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=44,
  serialized_end=122,
)


_SAMPLEDISC = _descriptor.Descriptor(
  name='SampleDisc',
  full_name='crypto.proto.RLWE.SampleDisc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='crypto.proto.RLWE.SampleDisc.a', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='b', full_name='crypto.proto.RLWE.SampleDisc.b', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=124,
  serialized_end=202,
)


_SAMPLERLWR = _descriptor.Descriptor(
  name='SampleRLWR',
  full_name='crypto.proto.RLWE.SampleRLWR',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='crypto.proto.RLWE.SampleRLWR.a', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='b', full_name='crypto.proto.RLWE.SampleRLWR.b', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=204,
  serialized_end=282,
)


_SAMPLECONTPRODUCT = _descriptor.Descriptor(
  name='SampleContProduct',
  full_name='crypto.proto.RLWE.SampleContProduct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='crypto.proto.RLWE.SampleContProduct.a', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='b', full_name='crypto.proto.RLWE.SampleContProduct.b', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=284,
  serialized_end=383,
)


_SAMPLEDISCPRODUCT = _descriptor.Descriptor(
  name='SampleDiscProduct',
  full_name='crypto.proto.RLWE.SampleDiscProduct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='crypto.proto.RLWE.SampleDiscProduct.a', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='b', full_name='crypto.proto.RLWE.SampleDiscProduct.b', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=385,
  serialized_end=484,
)


_SAMPLERLWRPRODUCT = _descriptor.Descriptor(
  name='SampleRLWRProduct',
  full_name='crypto.proto.RLWE.SampleRLWRProduct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='crypto.proto.RLWE.SampleRLWRProduct.a', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='b', full_name='crypto.proto.RLWE.SampleRLWRProduct.b', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=486,
  serialized_end=585,
)

_SAMPLECONT.fields_by_name['a'].message_type = Lol_pb2._RQ
_SAMPLECONT.fields_by_name['b'].message_type = Lol_pb2._KQ
_SAMPLEDISC.fields_by_name['a'].message_type = Lol_pb2._RQ
_SAMPLEDISC.fields_by_name['b'].message_type = Lol_pb2._RQ
_SAMPLERLWR.fields_by_name['a'].message_type = Lol_pb2._RQ
_SAMPLERLWR.fields_by_name['b'].message_type = Lol_pb2._RQ
_SAMPLECONTPRODUCT.fields_by_name['a'].message_type = Lol_pb2._RQPRODUCT
_SAMPLECONTPRODUCT.fields_by_name['b'].message_type = Lol_pb2._KQPRODUCT
_SAMPLEDISCPRODUCT.fields_by_name['a'].message_type = Lol_pb2._RQPRODUCT
_SAMPLEDISCPRODUCT.fields_by_name['b'].message_type = Lol_pb2._RQPRODUCT
_SAMPLERLWRPRODUCT.fields_by_name['a'].message_type = Lol_pb2._RQPRODUCT
_SAMPLERLWRPRODUCT.fields_by_name['b'].message_type = Lol_pb2._RQPRODUCT
DESCRIPTOR.message_types_by_name['SampleCont'] = _SAMPLECONT
DESCRIPTOR.message_types_by_name['SampleDisc'] = _SAMPLEDISC
DESCRIPTOR.message_types_by_name['SampleRLWR'] = _SAMPLERLWR
DESCRIPTOR.message_types_by_name['SampleContProduct'] = _SAMPLECONTPRODUCT
DESCRIPTOR.message_types_by_name['SampleDiscProduct'] = _SAMPLEDISCPRODUCT
DESCRIPTOR.message_types_by_name['SampleRLWRProduct'] = _SAMPLERLWRPRODUCT

SampleCont = _reflection.GeneratedProtocolMessageType('SampleCont', (_message.Message,), dict(
  DESCRIPTOR = _SAMPLECONT,
  __module__ = 'RLWE_pb2'
  # @@protoc_insertion_point(class_scope:crypto.proto.RLWE.SampleCont)
  ))
_sym_db.RegisterMessage(SampleCont)

SampleDisc = _reflection.GeneratedProtocolMessageType('SampleDisc', (_message.Message,), dict(
  DESCRIPTOR = _SAMPLEDISC,
  __module__ = 'RLWE_pb2'
  # @@protoc_insertion_point(class_scope:crypto.proto.RLWE.SampleDisc)
  ))
_sym_db.RegisterMessage(SampleDisc)

SampleRLWR = _reflection.GeneratedProtocolMessageType('SampleRLWR', (_message.Message,), dict(
  DESCRIPTOR = _SAMPLERLWR,
  __module__ = 'RLWE_pb2'
  # @@protoc_insertion_point(class_scope:crypto.proto.RLWE.SampleRLWR)
  ))
_sym_db.RegisterMessage(SampleRLWR)

SampleContProduct = _reflection.GeneratedProtocolMessageType('SampleContProduct', (_message.Message,), dict(
  DESCRIPTOR = _SAMPLECONTPRODUCT,
  __module__ = 'RLWE_pb2'
  # @@protoc_insertion_point(class_scope:crypto.proto.RLWE.SampleContProduct)
  ))
_sym_db.RegisterMessage(SampleContProduct)

SampleDiscProduct = _reflection.GeneratedProtocolMessageType('SampleDiscProduct', (_message.Message,), dict(
  DESCRIPTOR = _SAMPLEDISCPRODUCT,
  __module__ = 'RLWE_pb2'
  # @@protoc_insertion_point(class_scope:crypto.proto.RLWE.SampleDiscProduct)
  ))
_sym_db.RegisterMessage(SampleDiscProduct)

SampleRLWRProduct = _reflection.GeneratedProtocolMessageType('SampleRLWRProduct', (_message.Message,), dict(
  DESCRIPTOR = _SAMPLERLWRPRODUCT,
  __module__ = 'RLWE_pb2'
  # @@protoc_insertion_point(class_scope:crypto.proto.RLWE.SampleRLWRProduct)
  ))
_sym_db.RegisterMessage(SampleRLWRProduct)


# @@protoc_insertion_point(module_scope)