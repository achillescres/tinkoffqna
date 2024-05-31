from abc import ABC, abstractmethod


class AbstractQna(ABC):
    @abstractmethod
    def query_answer(self, query: str) -> (str, list[str]):
        pass


class QnaStub(AbstractQna):
    def query_answer(self, query: str) -> (str, list[str]):
        return "cool answer", ["google.com", "yandex.com"]
