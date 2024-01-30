# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: source.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0csource.proto\x12\tsource.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto"u\n\x0bReadRequest\x12/\n\x07request\x18\x01 \x01(\x0b\x32\x1e.source.v1.ReadRequest.Request\x1a\x35\n\x07Request\x12\x13\n\x0bnum_records\x18\x01 \x01(\x04\x12\x15\n\rtimeout_in_ms\x18\x02 \x01(\r"\xba\x01\n\x0cReadResponse\x12.\n\x06result\x18\x01 \x01(\x0b\x32\x1e.source.v1.ReadResponse.Result\x1az\n\x06Result\x12\x0f\n\x07payload\x18\x01 \x01(\x0c\x12!\n\x06offset\x18\x02 \x01(\x0b\x32\x11.source.v1.Offset\x12.\n\nevent_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04keys\x18\x04 \x03(\t"k\n\nAckRequest\x12.\n\x07request\x18\x01 \x01(\x0b\x32\x1d.source.v1.AckRequest.Request\x1a-\n\x07Request\x12"\n\x07offsets\x18\x01 \x03(\x0b\x32\x11.source.v1.Offset"o\n\x0b\x41\x63kResponse\x12-\n\x06result\x18\x01 \x01(\x0b\x32\x1d.source.v1.AckResponse.Result\x1a\x31\n\x06Result\x12\'\n\x07success\x18\x01 \x01(\x0b\x32\x16.google.protobuf.Empty"\x1e\n\rReadyResponse\x12\r\n\x05ready\x18\x01 \x01(\x08"]\n\x0fPendingResponse\x12\x31\n\x06result\x18\x01 \x01(\x0b\x32!.source.v1.PendingResponse.Result\x1a\x17\n\x06Result\x12\r\n\x05\x63ount\x18\x01 \x01(\x03"h\n\x12PartitionsResponse\x12\x34\n\x06result\x18\x01 \x01(\x0b\x32$.source.v1.PartitionsResponse.Result\x1a\x1c\n\x06Result\x12\x12\n\npartitions\x18\x01 \x03(\x05".\n\x06Offset\x12\x0e\n\x06offset\x18\x01 \x01(\x0c\x12\x14\n\x0cpartition_id\x18\x02 \x01(\x05\x32\xc2\x02\n\x06Source\x12;\n\x06ReadFn\x12\x16.source.v1.ReadRequest\x1a\x17.source.v1.ReadResponse0\x01\x12\x36\n\x05\x41\x63kFn\x12\x15.source.v1.AckRequest\x1a\x16.source.v1.AckResponse\x12?\n\tPendingFn\x12\x16.google.protobuf.Empty\x1a\x1a.source.v1.PendingResponse\x12\x45\n\x0cPartitionsFn\x12\x16.google.protobuf.Empty\x1a\x1d.source.v1.PartitionsResponse\x12;\n\x07IsReady\x12\x16.google.protobuf.Empty\x1a\x18.source.v1.ReadyResponseb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "source_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_READREQUEST"]._serialized_start = 89
    _globals["_READREQUEST"]._serialized_end = 206
    _globals["_READREQUEST_REQUEST"]._serialized_start = 153
    _globals["_READREQUEST_REQUEST"]._serialized_end = 206
    _globals["_READRESPONSE"]._serialized_start = 209
    _globals["_READRESPONSE"]._serialized_end = 395
    _globals["_READRESPONSE_RESULT"]._serialized_start = 273
    _globals["_READRESPONSE_RESULT"]._serialized_end = 395
    _globals["_ACKREQUEST"]._serialized_start = 397
    _globals["_ACKREQUEST"]._serialized_end = 504
    _globals["_ACKREQUEST_REQUEST"]._serialized_start = 459
    _globals["_ACKREQUEST_REQUEST"]._serialized_end = 504
    _globals["_ACKRESPONSE"]._serialized_start = 506
    _globals["_ACKRESPONSE"]._serialized_end = 617
    _globals["_ACKRESPONSE_RESULT"]._serialized_start = 568
    _globals["_ACKRESPONSE_RESULT"]._serialized_end = 617
    _globals["_READYRESPONSE"]._serialized_start = 619
    _globals["_READYRESPONSE"]._serialized_end = 649
    _globals["_PENDINGRESPONSE"]._serialized_start = 651
    _globals["_PENDINGRESPONSE"]._serialized_end = 744
    _globals["_PENDINGRESPONSE_RESULT"]._serialized_start = 721
    _globals["_PENDINGRESPONSE_RESULT"]._serialized_end = 744
    _globals["_PARTITIONSRESPONSE"]._serialized_start = 746
    _globals["_PARTITIONSRESPONSE"]._serialized_end = 850
    _globals["_PARTITIONSRESPONSE_RESULT"]._serialized_start = 822
    _globals["_PARTITIONSRESPONSE_RESULT"]._serialized_end = 850
    _globals["_OFFSET"]._serialized_start = 852
    _globals["_OFFSET"]._serialized_end = 898
    _globals["_SOURCE"]._serialized_start = 901
    _globals["_SOURCE"]._serialized_end = 1223
# @@protoc_insertion_point(module_scope)