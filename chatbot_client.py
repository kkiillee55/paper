"""
The client code for Chatbot.

You have to run ```python server_main.py``` to startup local server.
Then you can run ```python chatbot_client.py``` to start chatting with LLM.

"""

from protos import chatbot_pb2, chatbot_pb2_grpc
import grpc
import time

channel = grpc.insecure_channel('localhost:5000')
stub = chatbot_pb2_grpc.ChatbotStub(channel)


def question_iterator():
    i = 0
    while True:
        # The RPC call is async, wait for 20s before asking new question.
        time.sleep(20)
        if i == 0:
            # Need to initialize LLM first, specify create_new_model=True in ChatRequest.
            print('The first request is to initialize LLM model.')
            yield chatbot_pb2.ChatRequest(create_new_model=True)
        else:
            question = input("Input your question: \n")
            yield chatbot_pb2.ChatRequest(question=question)
        i += 1


for response in stub.Chat(question_iterator()):
    print(response, '\n')
