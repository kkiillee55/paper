This folder includes ```chatbot.proto``` which contains proto service definition and some generated python scripts.

To generate the code, run 
```python -m grpc_tools.protoc -I .\protos --python_out=.\protos --pyi_out=.\protos --grpc_python_out=.\protos .\protos\chatbot.proto```

Then in chatbot_pb2_grpc.py, change the import ```import chatbot_pb2 as chatbot__pb2``` to ```from . import chatbot_pb2 as chatbot__pb2```(It could be a bug or the cmd is incorrect).
