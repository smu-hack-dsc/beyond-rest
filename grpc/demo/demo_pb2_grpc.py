# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import demo_pb2 as demo__pb2


class DemoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetServerResponse = channel.unary_unary(
                '/demo.Demo/GetServerResponse',
                request_serializer=demo__pb2.Request.SerializeToString,
                response_deserializer=demo__pb2.Response.FromString,
                )
        self.GetMultipleServerResponse = channel.unary_stream(
                '/demo.Demo/GetMultipleServerResponse',
                request_serializer=demo__pb2.Request.SerializeToString,
                response_deserializer=demo__pb2.Response.FromString,
                )
        self.GetServerResponseJSON = channel.unary_unary(
                '/demo.Demo/GetServerResponseJSON',
                request_serializer=demo__pb2.Request.SerializeToString,
                response_deserializer=demo__pb2.Response.FromString,
                )


class DemoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetServerResponse(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMultipleServerResponse(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServerResponseJSON(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DemoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetServerResponse': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServerResponse,
                    request_deserializer=demo__pb2.Request.FromString,
                    response_serializer=demo__pb2.Response.SerializeToString,
            ),
            'GetMultipleServerResponse': grpc.unary_stream_rpc_method_handler(
                    servicer.GetMultipleServerResponse,
                    request_deserializer=demo__pb2.Request.FromString,
                    response_serializer=demo__pb2.Response.SerializeToString,
            ),
            'GetServerResponseJSON': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServerResponseJSON,
                    request_deserializer=demo__pb2.Request.FromString,
                    response_serializer=demo__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'demo.Demo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Demo(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetServerResponse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/demo.Demo/GetServerResponse',
            demo__pb2.Request.SerializeToString,
            demo__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMultipleServerResponse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/demo.Demo/GetMultipleServerResponse',
            demo__pb2.Request.SerializeToString,
            demo__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetServerResponseJSON(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/demo.Demo/GetServerResponseJSON',
            demo__pb2.Request.SerializeToString,
            demo__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
