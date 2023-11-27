from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChatRequest(_message.Message):
    __slots__ = ["question", "file", "create_new_model"]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    CREATE_NEW_MODEL_FIELD_NUMBER: _ClassVar[int]
    question: str
    file: bytes
    create_new_model: bool
    def __init__(self, question: _Optional[str] = ..., file: _Optional[bytes] = ..., create_new_model: bool = ...) -> None: ...

class ChatResponse(_message.Message):
    __slots__ = ["answer"]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    answer: str
    def __init__(self, answer: _Optional[str] = ...) -> None: ...
