# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import chatbot_pb2 as chatbot__pb2

class ChatbotStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Chat = channel.stream_stream(
                '/chatbot.Chatbot/Chat',
                request_serializer=chatbot__pb2.ChatRequest.SerializeToString,
                response_deserializer=chatbot__pb2.ChatResponse.FromString,
                )


class ChatbotServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Chat(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChatbotServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Chat': grpc.stream_stream_rpc_method_handler(
                    servicer.Chat,
                    request_deserializer=chatbot__pb2.ChatRequest.FromString,
                    response_serializer=chatbot__pb2.ChatResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'chatbot.Chatbot', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Chatbot(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Chat(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/chatbot.Chatbot/Chat',
            chatbot__pb2.ChatRequest.SerializeToString,
            chatbot__pb2.ChatResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)