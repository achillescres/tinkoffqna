import os

import chromadb
import httpx
from openai import OpenAI
from sentence_transformers import SentenceTransformer

from app.ai.qna import AbstractQna
from app.ai.v2.gptqna import EmbeddingModel, GptQna
from app.config import Config
from app.service.qna import QnaService

Config.read_from_env()

http_client = httpx.Client(proxy=Config.http_proxy_url)

openai_client = OpenAI(api_key=Config.openai_api_key, http_client=http_client)
model = SentenceTransformer(Config.sentence_transformer_model_name)
chroma_client = chromadb.HttpClient(host=Config.chroma_db_host, port=Config.chroma_db_port)
embedding_model = EmbeddingModel(model)
collection = chroma_client.get_collection(name="tinkoff_collection", embedding_function=embedding_model)

_gtp_qna_ai = GptQna(collection=collection, openai_client=openai_client)


def get_qna_ai() -> AbstractQna:
    return _gtp_qna_ai


def get_qna_service() -> QnaService:
    return QnaService(get_qna_ai())
