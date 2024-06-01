import numpy as np
import pandas as pd
from numpy import dot
from numpy.linalg import norm


def cosine_similarity(a, b):
    cos_sim = dot(a, b) / (norm(a) * norm(b))
    return cos_sim


def get_top_n_nearest_docs(text_embedded: np.array, docs_embedded: pd.DataFrame, n_neighbors: int):
    series = pd.Series(index=docs_embedded.index)
    for index in docs_embedded.index:
        cos_sim = cosine_similarity(text_embedded, docs_embedded.loc[index][:-1])
        series.loc[index] = cos_sim

    return series.sort_values(ascending=False).head(n_neighbors)
