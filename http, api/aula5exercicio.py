import pandas as pd
from pandas import json_normalize
import requests
import numpy as np

dados_usuarios = [
    {"id": 1, "nome": " Ana  ", "idade": "25", "cidade": "juiz de fora", "ativo": "true"},
    {"id": 2, "nome": "Bruno",  "idade": "30", "cidade": "SÃO PAULO",    "ativo": "false"},
    {"id": 3, "nome": "Carla",  "idade": None, "cidade": "rio de janeiro", "ativo": "true"},
    {"id": 3, "nome": "Carla",  "idade": None, "cidade": "rio de janeiro", "ativo": "true"}
]
df = pd.DataFrame(dados_usuarios)
print(df)

#Remover linhas duplicadas.
print(df.duplicated())
df = df.drop_duplicates()
print(df)

#Removendo espaços extras
df["nome"] = df["nome"].str.strip()
print(df["nome"])

#CORRIGINDO TIPOS DE DADOS
df['idade'] = pd.to_numeric(df['idade'], errors="coerce").astype("Int64")
print(df["idade"])
print(df.dtypes)

df['cidade'] = df["cidade"].str.title()
print(df["cidade"])

#converter a coluna ativo de strings para valores booleanos reais
mapeamento = {'true': True, 'false': False}
df['ativo'] = df['ativo'].str.lower().map(mapeamento)
print(df['ativo'])

#Preencher idades ausentes com a média das idades conhecidas.
media = df["idade"].mean()
df['idade'] = df['idade'].fillna(round(media))
df['idade'] = pd.to_numeric(df['idade']).astype("Int64")
print(f"Média aplicada: {media}")
print(df)


