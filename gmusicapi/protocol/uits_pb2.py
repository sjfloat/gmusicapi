# -*- coding: utf-8 -*-
from __future__ import (unicode_literals, print_function, division,
                        absolute_import)
from future import standard_library
standard_library.install_aliases()
from builtins import str
# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
from future.utils import with_metaclass
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='uits.proto',
  package='',
  serialized_pb='\n\nuits.proto\"k\n\tProductId\x12\x1d\n\x04type\x18\x01 \x02(\x0e\x32\x0f.ProductId.Type\x12\x18\n\tcompleted\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\n\n\x02id\x18\x03 \x02(\t\"\x19\n\x04Type\x12\x07\n\x03UPC\x10\x01\x12\x08\n\x04GRID\x10\x02\"D\n\x07\x41ssetId\x12\x1b\n\x04type\x18\x01 \x02(\x0e\x32\r.AssetId.Type\x12\n\n\x02id\x18\x02 \x02(\t\"\x10\n\x04Type\x12\x08\n\x04ISRC\x10\x01\"/\n\rTransactionId\x12\x12\n\x07version\x18\x01 \x02(\t:\x01\x31\x12\n\n\x02id\x18\x02 \x02(\t\"d\n\x07MediaId\x12.\n\x0e\x61lgorithm_type\x18\x01 \x02(\x0e\x32\x16.MediaId.AlgorithmType\x12\x0c\n\x04hash\x18\x02 \x02(\t\"\x1b\n\rAlgorithmType\x12\n\n\x06SHA256\x10\x01\"\x8b\x01\n\x07UrlInfo\x12\x1b\n\x04type\x18\x01 \x02(\x0e\x32\r.UrlInfo.Type\x12\x0b\n\x03url\x18\x02 \x02(\t\"V\n\x04Type\x12\x08\n\x04WCOM\x10\x01\x12\x08\n\x04WCOP\x10\x02\x12\x08\n\x04WOAF\x10\x03\x12\x08\n\x04WOAR\x10\x04\x12\x08\n\x04WOAS\x10\x05\x12\x08\n\x04WORS\x10\x06\x12\x08\n\x04WPAY\x10\x07\x12\x08\n\x04WPUB\x10\x08\"\x94\x01\n\x0f\x43opyrightStatus\x12#\n\x04type\x18\x01 \x02(\x0e\x32\x15.CopyrightStatus.Type\x12\x11\n\tcopyright\x18\x02 \x01(\t\"I\n\x04Type\x12\x0f\n\x0bUNSPECIFIED\x10\x01\x12\x15\n\x11\x41LLRIGHTSRESERVED\x10\x02\x12\x0e\n\nPRERELEASE\x10\x03\x12\t\n\x05OTHER\x10\x04\"$\n\x05\x45xtra\x12\x0c\n\x04type\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"\xb5\x03\n\x0cUitsMetadata\x12\r\n\x05nonce\x18\x01 \x02(\t\x12\x16\n\x0e\x64istributor_id\x18\x02 \x02(\t\x12\x18\n\x10transaction_date\x18\x03 \x02(\t\x12\x1e\n\nproduct_id\x18\x04 \x02(\x0b\x32\n.ProductId\x12\x1a\n\x08\x61sset_id\x18\x05 \x02(\x0b\x32\x08.AssetId\x12&\n\x0etransaction_id\x18\x06 \x02(\x0b\x32\x0e.TransactionId\x12\x1a\n\x08media_id\x18\x07 \x02(\x0b\x32\x08.MediaId\x12\x1a\n\x08url_info\x18\x08 \x01(\x0b\x32\x08.UrlInfo\x12\x42\n\x16parental_advisory_type\x18\t \x01(\x0e\x32\".UitsMetadata.ParentalAdvisoryType\x12*\n\x10\x63opyright_status\x18\n \x01(\x0b\x32\x10.CopyrightStatus\x12\x15\n\x05\x65xtra\x18\x0b \x03(\x0b\x32\x06.Extra\"A\n\x14ParentalAdvisoryType\x12\x0f\n\x0bUNSPECIFIED\x10\x01\x12\x0c\n\x08\x45XPLICIT\x10\x02\x12\n\n\x06\x45\x44ITED\x10\x03\"\xf5\x01\n\rUitsSignature\x12\x34\n\x0e\x61lgorithm_type\x18\x01 \x02(\x0e\x32\x1c.UitsSignature.AlgorithmType\x12\x42\n\x15\x63\x61nonicalization_type\x18\x02 \x02(\x0e\x32#.UitsSignature.CanonicalizationType\x12\x0e\n\x06key_id\x18\x03 \x02(\t\x12\r\n\x05value\x18\x04 \x02(\t\")\n\rAlgorithmType\x12\x0b\n\x07RSA2048\x10\x01\x12\x0b\n\x07\x44SA2048\x10\x02\" \n\x14\x43\x61nonicalizationType\x12\x08\n\x04NONE\x10\x01\"J\n\x04Uits\x12\x1f\n\x08metadata\x18\x01 \x02(\x0b\x32\r.UitsMetadata\x12!\n\tsignature\x18\x02 \x02(\x0b\x32\x0e.UitsSignature')



_PRODUCTID_TYPE = descriptor.EnumDescriptor(
  name='Type',
  full_name='ProductId.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='UPC', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='GRID', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=96,
  serialized_end=121,
)

_ASSETID_TYPE = descriptor.EnumDescriptor(
  name='Type',
  full_name='AssetId.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='ISRC', index=0, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=175,
  serialized_end=191,
)

_MEDIAID_ALGORITHMTYPE = descriptor.EnumDescriptor(
  name='AlgorithmType',
  full_name='MediaId.AlgorithmType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='SHA256', index=0, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=315,
  serialized_end=342,
)

_URLINFO_TYPE = descriptor.EnumDescriptor(
  name='Type',
  full_name='UrlInfo.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='WCOM', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='WCOP', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='WOAF', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='WOAR', index=3, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='WOAS', index=4, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='WORS', index=5, number=6,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='WPAY', index=6, number=7,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='WPUB', index=7, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=398,
  serialized_end=484,
)

_COPYRIGHTSTATUS_TYPE = descriptor.EnumDescriptor(
  name='Type',
  full_name='CopyrightStatus.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ALLRIGHTSRESERVED', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PRERELEASE', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='OTHER', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=562,
  serialized_end=635,
)

_UITSMETADATA_PARENTALADVISORYTYPE = descriptor.EnumDescriptor(
  name='ParentalAdvisoryType',
  full_name='UitsMetadata.ParentalAdvisoryType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='EXPLICIT', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='EDITED', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1048,
  serialized_end=1113,
)

_UITSSIGNATURE_ALGORITHMTYPE = descriptor.EnumDescriptor(
  name='AlgorithmType',
  full_name='UitsSignature.AlgorithmType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='RSA2048', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DSA2048', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1286,
  serialized_end=1327,
)

_UITSSIGNATURE_CANONICALIZATIONTYPE = descriptor.EnumDescriptor(
  name='CanonicalizationType',
  full_name='UitsSignature.CanonicalizationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1329,
  serialized_end=1361,
)


_PRODUCTID = descriptor.Descriptor(
  name='ProductId',
  full_name='ProductId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='ProductId.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='completed', full_name='ProductId.completed', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='ProductId.id', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=str(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PRODUCTID_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=14,
  serialized_end=121,
)


_ASSETID = descriptor.Descriptor(
  name='AssetId',
  full_name='AssetId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='AssetId.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='AssetId.id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=str(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ASSETID_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=123,
  serialized_end=191,
)


_TRANSACTIONID = descriptor.Descriptor(
  name='TransactionId',
  full_name='TransactionId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='version', full_name='TransactionId.version', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=True, default_value=str("1"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='TransactionId.id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=str(""),
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
  serialized_start=193,
  serialized_end=240,
)


_MEDIAID = descriptor.Descriptor(
  name='MediaId',
  full_name='MediaId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='algorithm_type', full_name='MediaId.algorithm_type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hash', full_name='MediaId.hash', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=str(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MEDIAID_ALGORITHMTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=242,
  serialized_end=342,
)


_URLINFO = descriptor.Descriptor(
  name='UrlInfo',
  full_name='UrlInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='UrlInfo.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='url', full_name='UrlInfo.url', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=str(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _URLINFO_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=345,
  serialized_end=484,
)


_COPYRIGHTSTATUS = descriptor.Descriptor(
  name='CopyrightStatus',
  full_name='CopyrightStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='CopyrightStatus.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='copyright', full_name='CopyrightStatus.copyright', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=str(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COPYRIGHTSTATUS_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=487,
  serialized_end=635,
)


_EXTRA = descriptor.Descriptor(
  name='Extra',
  full_name='Extra',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='Extra.type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=str(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='Extra.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=str(""),
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
  serialized_start=637,
  serialized_end=673,
)


_UITSMETADATA = descriptor.Descriptor(
  name='UitsMetadata',
  full_name='UitsMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='nonce', full_name='UitsMetadata.nonce', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=str(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='distributor_id', full_name='UitsMetadata.distributor_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=str(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='transaction_date', full_name='UitsMetadata.transaction_date', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=str(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='product_id', full_name='UitsMetadata.product_id', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='asset_id', full_name='UitsMetadata.asset_id', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='transaction_id', full_name='UitsMetadata.transaction_id', index=5,
      number=6, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='media_id', full_name='UitsMetadata.media_id', index=6,
      number=7, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='url_info', full_name='UitsMetadata.url_info', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='parental_advisory_type', full_name='UitsMetadata.parental_advisory_type', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='copyright_status', full_name='UitsMetadata.copyright_status', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extra', full_name='UitsMetadata.extra', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _UITSMETADATA_PARENTALADVISORYTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=676,
  serialized_end=1113,
)


_UITSSIGNATURE = descriptor.Descriptor(
  name='UitsSignature',
  full_name='UitsSignature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='algorithm_type', full_name='UitsSignature.algorithm_type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='canonicalization_type', full_name='UitsSignature.canonicalization_type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='key_id', full_name='UitsSignature.key_id', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=str(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='UitsSignature.value', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=str(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _UITSSIGNATURE_ALGORITHMTYPE,
    _UITSSIGNATURE_CANONICALIZATIONTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1116,
  serialized_end=1361,
)


_UITS = descriptor.Descriptor(
  name='Uits',
  full_name='Uits',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='metadata', full_name='Uits.metadata', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='signature', full_name='Uits.signature', index=1,
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
  serialized_start=1363,
  serialized_end=1437,
)

_PRODUCTID.fields_by_name['type'].enum_type = _PRODUCTID_TYPE
_PRODUCTID_TYPE.containing_type = _PRODUCTID;
_ASSETID.fields_by_name['type'].enum_type = _ASSETID_TYPE
_ASSETID_TYPE.containing_type = _ASSETID;
_MEDIAID.fields_by_name['algorithm_type'].enum_type = _MEDIAID_ALGORITHMTYPE
_MEDIAID_ALGORITHMTYPE.containing_type = _MEDIAID;
_URLINFO.fields_by_name['type'].enum_type = _URLINFO_TYPE
_URLINFO_TYPE.containing_type = _URLINFO;
_COPYRIGHTSTATUS.fields_by_name['type'].enum_type = _COPYRIGHTSTATUS_TYPE
_COPYRIGHTSTATUS_TYPE.containing_type = _COPYRIGHTSTATUS;
_UITSMETADATA.fields_by_name['product_id'].message_type = _PRODUCTID
_UITSMETADATA.fields_by_name['asset_id'].message_type = _ASSETID
_UITSMETADATA.fields_by_name['transaction_id'].message_type = _TRANSACTIONID
_UITSMETADATA.fields_by_name['media_id'].message_type = _MEDIAID
_UITSMETADATA.fields_by_name['url_info'].message_type = _URLINFO
_UITSMETADATA.fields_by_name['parental_advisory_type'].enum_type = _UITSMETADATA_PARENTALADVISORYTYPE
_UITSMETADATA.fields_by_name['copyright_status'].message_type = _COPYRIGHTSTATUS
_UITSMETADATA.fields_by_name['extra'].message_type = _EXTRA
_UITSMETADATA_PARENTALADVISORYTYPE.containing_type = _UITSMETADATA;
_UITSSIGNATURE.fields_by_name['algorithm_type'].enum_type = _UITSSIGNATURE_ALGORITHMTYPE
_UITSSIGNATURE.fields_by_name['canonicalization_type'].enum_type = _UITSSIGNATURE_CANONICALIZATIONTYPE
_UITSSIGNATURE_ALGORITHMTYPE.containing_type = _UITSSIGNATURE;
_UITSSIGNATURE_CANONICALIZATIONTYPE.containing_type = _UITSSIGNATURE;
_UITS.fields_by_name['metadata'].message_type = _UITSMETADATA
_UITS.fields_by_name['signature'].message_type = _UITSSIGNATURE
DESCRIPTOR.message_types_by_name['ProductId'] = _PRODUCTID
DESCRIPTOR.message_types_by_name['AssetId'] = _ASSETID
DESCRIPTOR.message_types_by_name['TransactionId'] = _TRANSACTIONID
DESCRIPTOR.message_types_by_name['MediaId'] = _MEDIAID
DESCRIPTOR.message_types_by_name['UrlInfo'] = _URLINFO
DESCRIPTOR.message_types_by_name['CopyrightStatus'] = _COPYRIGHTSTATUS
DESCRIPTOR.message_types_by_name['Extra'] = _EXTRA
DESCRIPTOR.message_types_by_name['UitsMetadata'] = _UITSMETADATA
DESCRIPTOR.message_types_by_name['UitsSignature'] = _UITSSIGNATURE
DESCRIPTOR.message_types_by_name['Uits'] = _UITS

class ProductId(with_metaclass(reflection.GeneratedProtocolMessageType, message.Message)):
  DESCRIPTOR = _PRODUCTID

  # @@protoc_insertion_point(class_scope:ProductId)

class AssetId(with_metaclass(reflection.GeneratedProtocolMessageType, message.Message)):
  DESCRIPTOR = _ASSETID

  # @@protoc_insertion_point(class_scope:AssetId)

class TransactionId(with_metaclass(reflection.GeneratedProtocolMessageType, message.Message)):
  DESCRIPTOR = _TRANSACTIONID

  # @@protoc_insertion_point(class_scope:TransactionId)

class MediaId(with_metaclass(reflection.GeneratedProtocolMessageType, message.Message)):
  DESCRIPTOR = _MEDIAID

  # @@protoc_insertion_point(class_scope:MediaId)

class UrlInfo(with_metaclass(reflection.GeneratedProtocolMessageType, message.Message)):
  DESCRIPTOR = _URLINFO

  # @@protoc_insertion_point(class_scope:UrlInfo)

class CopyrightStatus(with_metaclass(reflection.GeneratedProtocolMessageType, message.Message)):
  DESCRIPTOR = _COPYRIGHTSTATUS

  # @@protoc_insertion_point(class_scope:CopyrightStatus)

class Extra(with_metaclass(reflection.GeneratedProtocolMessageType, message.Message)):
  DESCRIPTOR = _EXTRA

  # @@protoc_insertion_point(class_scope:Extra)

class UitsMetadata(with_metaclass(reflection.GeneratedProtocolMessageType, message.Message)):
  DESCRIPTOR = _UITSMETADATA

  # @@protoc_insertion_point(class_scope:UitsMetadata)

class UitsSignature(with_metaclass(reflection.GeneratedProtocolMessageType, message.Message)):
  DESCRIPTOR = _UITSSIGNATURE

  # @@protoc_insertion_point(class_scope:UitsSignature)

class Uits(with_metaclass(reflection.GeneratedProtocolMessageType, message.Message)):
  DESCRIPTOR = _UITS

  # @@protoc_insertion_point(class_scope:Uits)

# @@protoc_insertion_point(module_scope)
