from .ai.qna import AbstractQna, QnaStub
from .service.qna import QnaService


def get_qna_ai() -> AbstractQna:
    return QnaStub()


def get_qna_service():
    return QnaService(get_qna_ai())
