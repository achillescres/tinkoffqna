import os
import logging as log
import sys

from dotenv import load_dotenv


class Config:
    port: int
    http_proxy_url: str
    openai_api_key: str
    # yandex_embedding_api_key: str
    # yandex_embedding_url: str
    # yandex_embedding_model_uri: str
    # yandex_embedding_folder_key: str
    sentence_transformer_model_name: str
    chroma_db_host: str
    chroma_db_port: int

    @classmethod
    def read_from_env(cls):
        print(os.getcwd())
        load_dotenv(".env", verbose=True)
        port = os.environ.get("PORT")
        if port is None:
            log.critical("port is None")
            sys.exit(1)
        cls.port = int(port)
        # cls.yandex_embedding_api_key = os.environ.get("YANDEX_EMBEDDING_API_KEY")
        # cls.yandex_embedding_url = os.environ.get("YANDEX_EMBEDDING_URL")
        # cls.yandex_embedding_model_uri = os.environ.get("YANDEX_EMBEDDING_MODEL_URI")
        # cls.yandex_embedding_folder_key = os.environ.get("YANDEX_EMBEDDING_FOLDER_KEY")

        cls.http_proxy_url = os.environ.get("HTTP_PROXY_URL")
        cls.openai_api_key = os.environ.get("OPENAI_API_KEY")

        cls.sentence_transformer_model_name = os.environ.get("SENTENCE_TRANSFORMER_MODEL_NAME")
        cls.chroma_db_host = os.environ.get("CHROMA_DB_HOST")
        chroma_db_port = os.environ.get("CHROMA_DB_PORT")
        if chroma_db_port is None:
            log.critical("chroma_db_port is None")
            sys.exit(1)
        cls.chroma_db_port = int(chroma_db_port)

        for var, val in vars(cls).items():
            if "__" in var:
                continue
            if val is None:
                log.critical(f"{var} is None")
                sys.exit(1)
