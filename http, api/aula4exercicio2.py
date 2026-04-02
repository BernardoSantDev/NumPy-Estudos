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




usuarios = [
    {
        "id": 1,
        "nome": "Ana",
        "endereco": {
            "cidade": "Juiz de Fora",
            "estado": "MG"
        },
        "planos": ["básico", "data-science"]
    },
    {
        "id": 2,
        "nome": "Bruno",
        "endereco": {
            "cidade": "São Paulo",
            "estado": "SP"
        },
        "planos": ["premium"]
    },
    {
        "id": 3,
        "nome": "Carla",
        "endereco": {
            "cidade": "Rio de Janeiro",
            "estado": "RJ"
        },
        "planos": ["básico"]
    }
]


df = json_normalize(usuarios)
print("Colunas disponíveis:", df.columns.tolist())

colunas_interesse = [
    "id",
    "nome",
    "endereco.cidade",
    "endereco.estado"]

df_simplificado = df[colunas_interesse].rename(
    columns={
        "endereco.cidade": "cidade",
        "endereco.estado": "estado"
    }
)
print(df_simplificado.head())

filtro = df['planos'].astype(str).str.contains('data-science')
df_data_science = df[filtro]
print(df_data_science)