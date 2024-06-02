import numpy as np
import requests


class YandexEmbedding:
    api_key: str
    url: str
    model_uri: str
    folder_key: str

    def __init__(
            self,
            api_key: str,
            url: str,
            model_uri: str,
            folder_key: str
    ):
        self.api_key = api_key
        self.url = url
        self.model_uri = model_uri
        self.folder_key = folder_key

    @property
    def _headers(self) -> dict:
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
            "x-folder-id": f"{self.folder_key}"
        }

    def get_embedding(self, text: str, text_type: str = "query") -> np.array:
        print()
        query_data = {
            "modelUri": self.model_uri,
            "text": text,
        }

        return np.array(requests.post(self.url, json=query_data, headers=self._headers).json()["embedding"])
