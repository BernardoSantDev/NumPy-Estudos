#Busca users da API de teste.
#Converte para Python.
#Usa json_normalize para “abrir” os campos aninhados (address, company, etc.).
#Seleciona apenas as colunas que nos interessam.
#Renomeia colunas para nomes mais amigáveis.
#Mostra as primeiras linhas e o info().

import requests
import pandas as pd
from pandas import json_normalize

url = "https://jsonplaceholder.typicode.com/users"
resposta = requests.get(url)
resposta.raise_for_status()
dados = resposta.json()
print(type(dados))
df = json_normalize(dados)
print(df.head())
colunas_interesse = [
    "id",
    "name",
    "email",
    "address.city",
    "address.street",
    "company.name"
]
df_simplificado = df[colunas_interesse].rename(
    columns={
        "name": "nome",
        "address.city": "cidade",
        "address.street": "rua",
        "company.name": "empresa"
    }
)

print("\nDataFrame simplificado:")
print(df_simplificado.head())
print("\nInfo:")
print(df_simplificado.info())
