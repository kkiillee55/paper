from concurrent import futures
import logging

import grpc
from protos import chatbot_pb2, chatbot_pb2_grpc
from grpc_status import rpc_status
from google.rpc import status_pb2, code_pb2

from initialize_gpt_assistant import dummy_create_model


class ChatBotServer(chatbot_pb2_grpc.ChatbotServicer):
    def __init__(self):
        # Nothing to init now.
        self.father = "Ambrose"

    def Chat(self, request_iterator, context):
        # The LLM model to chat.
        model = None
        for chat_request in request_iterator:
            # Initialize LLM model if create_new_model=True.
            if chat_request.create_new_model:
                # TODO(@irene1391) Dummy function to create new LLM model, need to replace it with create_model() and ingest user uploaded file.
                model = dummy_create_model()
                yield chatbot_pb2.ChatResponse(answer="LLM initialized")
            else:
                if model is None:
                    # Raise error if the model is not initialized.
                    context.abort_with_status(rpc_status.to_status(status_pb2.Status(
                        code=code_pb2.RESOURCE_EXHAUSTED,
                        message="The model was not initialized",
                    )))
                if not chat_request.question:
                    # Notify if the user input is empty.
                    yield chatbot_pb2.ChatResponse(answer="Question is empty")
                else:
                    # Answer the user question with LLM.
                    answer = model(chat_request.question)
                    yield chatbot_pb2.ChatResponse(answer=answer['answer'])


if __name__ == '__main__':
    logging.basicConfig()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chatbot_pb2_grpc.add_ChatbotServicer_to_server(
        ChatBotServer(), server
    )
    server_addr = "localhost:5000"
    server.add_insecure_port(server_addr)
    server.start()
    print("Server started at " ,server_addr)
    server.wait_for_termination()
