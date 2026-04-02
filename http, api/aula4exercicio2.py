import pandas as pd
import requests
from pandas import json_normalize

produtos = [
    {"id": 1, "nome": "Teclado Mecânico", "preco": 250.0, "estoque": 10},
    {"id": 2, "nome": "Mouse Gamer",      "preco": 150.0, "estoque": 0},
    {"id": 3, "nome": "Monitor 24\"",     "preco": 900.0, "estoque": 5},
    {"id": 4, "nome": "Cadeira Gamer",    "preco": 1200.0, "estoque": 2}
]

df_produtos = pd.DataFrame(produtos)
print(df_produtos.head())
print(df_produtos.info())

import numpy as np
df_produtos['em_estoque'] = np.where(df_produtos['estoque'] > 0, 'Sim', 'Não')
print(df_produtos.head())


precos_disponiveis = df_produtos.loc[df_produtos['em_estoque'] == 'Sim', 'preco'].mean()
print(precos_disponiveis)