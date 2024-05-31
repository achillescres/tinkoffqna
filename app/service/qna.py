from app.ai.qna import AbstractQna


class QnaService:
    def __init__(self, qna: AbstractQna):
        self.qna = qna

    def query_answer(self, query: str) -> (str, list[str]):
        answer, links = self.qna.query_answer(query)
        # ...

        return answer, links
