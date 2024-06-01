import os

import httpx
import pandas as pd
from openai import OpenAI

from .ai.gpt.gpt import GptQna
from .ai.gpt.yandexembedding import YandexEmbedding
from .ai.qna import AbstractQna
from .service.qna import QnaService

with open('app/ai/gpt/questions_tinkoff.txt', 'r') as f:
    files = [line[:-1] for line in f.readlines()]


def get_qna_ai() -> AbstractQna:
    yandex_emb = YandexEmbedding(
        api_key=os.environ.get("YANDEX_EMBEDDING_API_KEY"),
        url=os.environ.get("YANDEX_EMBEDDING_URL"),
        model_uri=os.environ.get("YANDEX_EMBEDDING_MODEL_URI"),
        folder_key=os.environ.get("YANDEX_EMBEDDING_FOLDER_KEY")
    )

    http_client = httpx.Client(proxy=os.environ.get("HTTP_PROXY_URL"))

    print(os.environ.get("OPEN_AI_API_KEY"))
    open_ai = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),
                     http_client=http_client)
    embeddings: pd.DataFrame = pd.read_csv('app/ai/gpt/embeddings.csv')

    return GptQna(open_ai_client=open_ai, outer_embedding=yandex_emb, embeddings=embeddings, questions=files)


def get_qna_service() -> QnaService:
    return QnaService(get_qna_ai())
