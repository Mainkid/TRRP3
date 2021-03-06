# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: route_guide.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='route_guide.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11route_guide.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"3\n\x07Session\x12\x0c\n\x04hall\x18\x01 \x01(\x05\x12\x0c\n\x04\x66ilm\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\t\"E\n\x04\x46ilm\x12\r\n\x05genre\x18\x01 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x02 \x01(\t\x12\x0e\n\x06rating\x18\x03 \x01(\t\x12\r\n\x05title\x18\x04 \x01(\t\"\x17\n\x07\x43ountry\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x15\n\x05Genre\x12\x0c\n\x04name\x18\x01 \x01(\t\"<\n\x04Hall\x12\x10\n\x08\x63\x61pacity\x18\x01 \x01(\x05\x12\x11\n\thall_type\x18\x02 \x01(\t\x12\x0f\n\x07hall_no\x18\x03 \x01(\x05\"\x18\n\x06Result\x12\x0e\n\x06result\x18\x01 \x01(\t2\xb5\x01\n\nRouteGuide\x12#\n\nAddCountry\x12\x08.Country\x1a\x07.Result\"\x00(\x01\x12\x1f\n\x08\x41\x64\x64Genre\x12\x06.Genre\x1a\x07.Result\"\x00(\x01\x12\x1d\n\x07\x41\x64\x64Hall\x12\x05.Hall\x1a\x07.Result\"\x00(\x01\x12\x1d\n\x07\x41\x64\x64\x46ilm\x12\x05.Film\x1a\x07.Result\"\x00(\x01\x12#\n\nAddSession\x12\x08.Session\x1a\x07.Result\"\x00(\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_SESSION = _descriptor.Descriptor(
  name='Session',
  full_name='Session',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hall', full_name='Session.hall', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='film', full_name='Session.film', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time', full_name='Session.time', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=54,
  serialized_end=105,
)


_FILM = _descriptor.Descriptor(
  name='Film',
  full_name='Film',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='genre', full_name='Film.genre', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='country', full_name='Film.country', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rating', full_name='Film.rating', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='Film.title', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=107,
  serialized_end=176,
)


_COUNTRY = _descriptor.Descriptor(
  name='Country',
  full_name='Country',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Country.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=178,
  serialized_end=201,
)


_GENRE = _descriptor.Descriptor(
  name='Genre',
  full_name='Genre',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Genre.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=203,
  serialized_end=224,
)


_HALL = _descriptor.Descriptor(
  name='Hall',
  full_name='Hall',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='capacity', full_name='Hall.capacity', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hall_type', full_name='Hall.hall_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hall_no', full_name='Hall.hall_no', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=226,
  serialized_end=286,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='Result.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=288,
  serialized_end=312,
)

DESCRIPTOR.message_types_by_name['Session'] = _SESSION
DESCRIPTOR.message_types_by_name['Film'] = _FILM
DESCRIPTOR.message_types_by_name['Country'] = _COUNTRY
DESCRIPTOR.message_types_by_name['Genre'] = _GENRE
DESCRIPTOR.message_types_by_name['Hall'] = _HALL
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Session = _reflection.GeneratedProtocolMessageType('Session', (_message.Message,), {
  'DESCRIPTOR' : _SESSION,
  '__module__' : 'route_guide_pb2'
  # @@protoc_insertion_point(class_scope:Session)
  })
_sym_db.RegisterMessage(Session)

Film = _reflection.GeneratedProtocolMessageType('Film', (_message.Message,), {
  'DESCRIPTOR' : _FILM,
  '__module__' : 'route_guide_pb2'
  # @@protoc_insertion_point(class_scope:Film)
  })
_sym_db.RegisterMessage(Film)

Country = _reflection.GeneratedProtocolMessageType('Country', (_message.Message,), {
  'DESCRIPTOR' : _COUNTRY,
  '__module__' : 'route_guide_pb2'
  # @@protoc_insertion_point(class_scope:Country)
  })
_sym_db.RegisterMessage(Country)

Genre = _reflection.GeneratedProtocolMessageType('Genre', (_message.Message,), {
  'DESCRIPTOR' : _GENRE,
  '__module__' : 'route_guide_pb2'
  # @@protoc_insertion_point(class_scope:Genre)
  })
_sym_db.RegisterMessage(Genre)

Hall = _reflection.GeneratedProtocolMessageType('Hall', (_message.Message,), {
  'DESCRIPTOR' : _HALL,
  '__module__' : 'route_guide_pb2'
  # @@protoc_insertion_point(class_scope:Hall)
  })
_sym_db.RegisterMessage(Hall)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
  'DESCRIPTOR' : _RESULT,
  '__module__' : 'route_guide_pb2'
  # @@protoc_insertion_point(class_scope:Result)
  })
_sym_db.RegisterMessage(Result)



_ROUTEGUIDE = _descriptor.ServiceDescriptor(
  name='RouteGuide',
  full_name='RouteGuide',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=315,
  serialized_end=496,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddCountry',
    full_name='RouteGuide.AddCountry',
    index=0,
    containing_service=None,
    input_type=_COUNTRY,
    output_type=_RESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddGenre',
    full_name='RouteGuide.AddGenre',
    index=1,
    containing_service=None,
    input_type=_GENRE,
    output_type=_RESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddHall',
    full_name='RouteGuide.AddHall',
    index=2,
    containing_service=None,
    input_type=_HALL,
    output_type=_RESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddFilm',
    full_name='RouteGuide.AddFilm',
    index=3,
    containing_service=None,
    input_type=_FILM,
    output_type=_RESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddSession',
    full_name='RouteGuide.AddSession',
    index=4,
    containing_service=None,
    input_type=_SESSION,
    output_type=_RESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROUTEGUIDE)

DESCRIPTOR.services_by_name['RouteGuide'] = _ROUTEGUIDE

# @@protoc_insertion_point(module_scope)
