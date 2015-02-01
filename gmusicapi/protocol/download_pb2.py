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
  name='download.proto',
  package='',
  serialized_pb='\n\x0e\x64ownload.proto\"\xdf\x01\n\x18GetTracksToExportRequest\x12\x11\n\tclient_id\x18\x02 \x02(\t\x12\x1a\n\x12\x63ontinuation_token\x18\x03 \x01(\t\x12\x41\n\x0b\x65xport_type\x18\x04 \x01(\x0e\x32,.GetTracksToExportRequest.TracksToExportType\x12\x13\n\x0bupdated_min\x18\x05 \x01(\x03\"<\n\x12TracksToExportType\x12\x07\n\x03\x41LL\x10\x01\x12\x1d\n\x19PURCHASED_AND_PROMOTIONAL\x10\x02\"\x8d\x01\n\x11\x44ownloadTrackInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\r\n\x05\x61lbum\x18\x03 \x01(\t\x12\x14\n\x0c\x61lbum_artist\x18\x04 \x01(\t\x12\x0e\n\x06\x61rtist\x18\x05 \x01(\t\x12\x14\n\x0ctrack_number\x18\x06 \x01(\x05\x12\x12\n\ntrack_size\x18\x07 \x01(\x03\"\xd3\x02\n\x19GetTracksToExportResponse\x12?\n\x06status\x18\x01 \x02(\x0e\x32/.GetTracksToExportResponse.TracksToExportStatus\x12/\n\x13\x64ownload_track_info\x18\x02 \x03(\x0b\x32\x12.DownloadTrackInfo\x12\x1a\n\x12\x63ontinuation_token\x18\x03 \x01(\t\x12\x13\n\x0bupdated_min\x18\x04 \x01(\x03\"\x92\x01\n\x14TracksToExportStatus\x12\x06\n\x02OK\x10\x01\x12\x13\n\x0fTRANSIENT_ERROR\x10\x02\x12\x1b\n\x17MAX_NUM_CLIENTS_REACHED\x10\x03\x12!\n\x1dUNABLE_TO_AUTHENTICATE_CLIENT\x10\x04\x12\x1d\n\x19UNABLE_TO_REGISTER_CLIENT\x10\x05')



_GETTRACKSTOEXPORTREQUEST_TRACKSTOEXPORTTYPE = descriptor.EnumDescriptor(
  name='TracksToExportType',
  full_name='GetTracksToExportRequest.TracksToExportType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='ALL', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PURCHASED_AND_PROMOTIONAL', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=182,
  serialized_end=242,
)

_GETTRACKSTOEXPORTRESPONSE_TRACKSTOEXPORTSTATUS = descriptor.EnumDescriptor(
  name='TracksToExportStatus',
  full_name='GetTracksToExportResponse.TracksToExportStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='OK', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TRANSIENT_ERROR', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='MAX_NUM_CLIENTS_REACHED', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='UNABLE_TO_AUTHENTICATE_CLIENT', index=3, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='UNABLE_TO_REGISTER_CLIENT', index=4, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=582,
  serialized_end=728,
)


_GETTRACKSTOEXPORTREQUEST = descriptor.Descriptor(
  name='GetTracksToExportRequest',
  full_name='GetTracksToExportRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='client_id', full_name='GetTracksToExportRequest.client_id', index=0,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=str(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='continuation_token', full_name='GetTracksToExportRequest.continuation_token', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=str(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='export_type', full_name='GetTracksToExportRequest.export_type', index=2,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='updated_min', full_name='GetTracksToExportRequest.updated_min', index=3,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETTRACKSTOEXPORTREQUEST_TRACKSTOEXPORTTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=19,
  serialized_end=242,
)


_DOWNLOADTRACKINFO = descriptor.Descriptor(
  name='DownloadTrackInfo',
  full_name='DownloadTrackInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='DownloadTrackInfo.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=str(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='title', full_name='DownloadTrackInfo.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=str(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='album', full_name='DownloadTrackInfo.album', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=str(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='album_artist', full_name='DownloadTrackInfo.album_artist', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=str(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='artist', full_name='DownloadTrackInfo.artist', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=str(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='track_number', full_name='DownloadTrackInfo.track_number', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='track_size', full_name='DownloadTrackInfo.track_size', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=245,
  serialized_end=386,
)


_GETTRACKSTOEXPORTRESPONSE = descriptor.Descriptor(
  name='GetTracksToExportResponse',
  full_name='GetTracksToExportResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='status', full_name='GetTracksToExportResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='download_track_info', full_name='GetTracksToExportResponse.download_track_info', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='continuation_token', full_name='GetTracksToExportResponse.continuation_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=str(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='updated_min', full_name='GetTracksToExportResponse.updated_min', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETTRACKSTOEXPORTRESPONSE_TRACKSTOEXPORTSTATUS,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=389,
  serialized_end=728,
)

_GETTRACKSTOEXPORTREQUEST.fields_by_name['export_type'].enum_type = _GETTRACKSTOEXPORTREQUEST_TRACKSTOEXPORTTYPE
_GETTRACKSTOEXPORTREQUEST_TRACKSTOEXPORTTYPE.containing_type = _GETTRACKSTOEXPORTREQUEST;
_GETTRACKSTOEXPORTRESPONSE.fields_by_name['status'].enum_type = _GETTRACKSTOEXPORTRESPONSE_TRACKSTOEXPORTSTATUS
_GETTRACKSTOEXPORTRESPONSE.fields_by_name['download_track_info'].message_type = _DOWNLOADTRACKINFO
_GETTRACKSTOEXPORTRESPONSE_TRACKSTOEXPORTSTATUS.containing_type = _GETTRACKSTOEXPORTRESPONSE;
DESCRIPTOR.message_types_by_name['GetTracksToExportRequest'] = _GETTRACKSTOEXPORTREQUEST
DESCRIPTOR.message_types_by_name['DownloadTrackInfo'] = _DOWNLOADTRACKINFO
DESCRIPTOR.message_types_by_name['GetTracksToExportResponse'] = _GETTRACKSTOEXPORTRESPONSE

class GetTracksToExportRequest(with_metaclass(reflection.GeneratedProtocolMessageType, message.Message)):
  DESCRIPTOR = _GETTRACKSTOEXPORTREQUEST

  # @@protoc_insertion_point(class_scope:GetTracksToExportRequest)

class DownloadTrackInfo(with_metaclass(reflection.GeneratedProtocolMessageType, message.Message)):
  DESCRIPTOR = _DOWNLOADTRACKINFO

  # @@protoc_insertion_point(class_scope:DownloadTrackInfo)

class GetTracksToExportResponse(with_metaclass(reflection.GeneratedProtocolMessageType, message.Message)):
  DESCRIPTOR = _GETTRACKSTOEXPORTRESPONSE

  # @@protoc_insertion_point(class_scope:GetTracksToExportResponse)

# @@protoc_insertion_point(module_scope)
