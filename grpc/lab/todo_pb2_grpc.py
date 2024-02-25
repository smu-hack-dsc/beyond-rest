# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import todo_pb2 as todo__pb2


class TodoServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddTask = channel.unary_unary(
                '/todo.TodoService/AddTask',
                request_serializer=todo__pb2.TaskRequest.SerializeToString,
                response_deserializer=todo__pb2.TaskResponse.FromString,
                )
        self.GetTasks = channel.unary_unary(
                '/todo.TodoService/GetTasks',
                request_serializer=todo__pb2.Empty.SerializeToString,
                response_deserializer=todo__pb2.TasksList.FromString,
                )
        self.RemoveAllTasks = channel.unary_unary(
                '/todo.TodoService/RemoveAllTasks',
                request_serializer=todo__pb2.Empty.SerializeToString,
                response_deserializer=todo__pb2.TaskResponse.FromString,
                )
        self.GetTaskHistory = channel.unary_stream(
                '/todo.TodoService/GetTaskHistory',
                request_serializer=todo__pb2.Empty.SerializeToString,
                response_deserializer=todo__pb2.TaskResponse.FromString,
                )
        self.AddMultipleTasks = channel.stream_unary(
                '/todo.TodoService/AddMultipleTasks',
                request_serializer=todo__pb2.TaskRequest.SerializeToString,
                response_deserializer=todo__pb2.TaskResponse.FromString,
                )


class TodoServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddTask(self, request, context):
        """Implement Unary RPCs -> client send single request and server returns single response
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTasks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveAllTasks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTaskHistory(self, request, context):
        """Server streaming RPCs -> client send single request and server returns stream of responses
        gRPC guarantees the ordering of messages within an individual RPC call
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddMultipleTasks(self, request_iterator, context):
        """Client streaming RPCs -> client send sequence of messages and server reads all messages before sending back single response
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TodoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddTask': grpc.unary_unary_rpc_method_handler(
                    servicer.AddTask,
                    request_deserializer=todo__pb2.TaskRequest.FromString,
                    response_serializer=todo__pb2.TaskResponse.SerializeToString,
            ),
            'GetTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTasks,
                    request_deserializer=todo__pb2.Empty.FromString,
                    response_serializer=todo__pb2.TasksList.SerializeToString,
            ),
            'RemoveAllTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveAllTasks,
                    request_deserializer=todo__pb2.Empty.FromString,
                    response_serializer=todo__pb2.TaskResponse.SerializeToString,
            ),
            'GetTaskHistory': grpc.unary_stream_rpc_method_handler(
                    servicer.GetTaskHistory,
                    request_deserializer=todo__pb2.Empty.FromString,
                    response_serializer=todo__pb2.TaskResponse.SerializeToString,
            ),
            'AddMultipleTasks': grpc.stream_unary_rpc_method_handler(
                    servicer.AddMultipleTasks,
                    request_deserializer=todo__pb2.TaskRequest.FromString,
                    response_serializer=todo__pb2.TaskResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'todo.TodoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TodoService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todo.TodoService/AddTask',
            todo__pb2.TaskRequest.SerializeToString,
            todo__pb2.TaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTasks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todo.TodoService/GetTasks',
            todo__pb2.Empty.SerializeToString,
            todo__pb2.TasksList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveAllTasks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todo.TodoService/RemoveAllTasks',
            todo__pb2.Empty.SerializeToString,
            todo__pb2.TaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTaskHistory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/todo.TodoService/GetTaskHistory',
            todo__pb2.Empty.SerializeToString,
            todo__pb2.TaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddMultipleTasks(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/todo.TodoService/AddMultipleTasks',
            todo__pb2.TaskRequest.SerializeToString,
            todo__pb2.TaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
