# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import builds.service_pb2 as service__pb2


class TaskServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddTask = channel.unary_unary(
                '/TaskService/AddTask',
                request_serializer=service__pb2.Task.SerializeToString,
                response_deserializer=service__pb2.Null.FromString,
                )
        self.GetTask = channel.unary_unary(
                '/TaskService/GetTask',
                request_serializer=service__pb2.GetTaskArg.SerializeToString,
                response_deserializer=service__pb2.Task.FromString,
                )
        self.GetAllTasks = channel.unary_unary(
                '/TaskService/GetAllTasks',
                request_serializer=service__pb2.GetAllTasksArg.SerializeToString,
                response_deserializer=service__pb2.TaskList.FromString,
                )


class TaskServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllTasks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TaskServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddTask': grpc.unary_unary_rpc_method_handler(
                    servicer.AddTask,
                    request_deserializer=service__pb2.Task.FromString,
                    response_serializer=service__pb2.Null.SerializeToString,
            ),
            'GetTask': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTask,
                    request_deserializer=service__pb2.GetTaskArg.FromString,
                    response_serializer=service__pb2.Task.SerializeToString,
            ),
            'GetAllTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllTasks,
                    request_deserializer=service__pb2.GetAllTasksArg.FromString,
                    response_serializer=service__pb2.TaskList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TaskService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TaskService(object):
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
        return grpc.experimental.unary_unary(request, target, '/TaskService/AddTask',
            service__pb2.Task.SerializeToString,
            service__pb2.Null.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TaskService/GetTask',
            service__pb2.GetTaskArg.SerializeToString,
            service__pb2.Task.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllTasks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TaskService/GetAllTasks',
            service__pb2.GetAllTasksArg.SerializeToString,
            service__pb2.TaskList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)