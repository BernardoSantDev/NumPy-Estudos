import pandas as pd
import requests

dados = [
    {"id": 1, "nome": "Ana",   "idade": 28, "cidade": "Juiz de Fora"},
    {"id": 2, "nome": "Bruno", "idade": 22, "cidade": "São Paulo"},
    {"id": 3, "nome": "Carla", "idade": 31, "cidade": "Rio de Janeiro"}
]

df = pd.DataFrame(dados)
print(df)



usuario = {"id": 1, "nome": "Ana", "idade": 28}
df = pd.DataFrame([usuario])
print(df)



url = "https://jsonplaceholder.typicode.com/users"
resposta = requests.get(url)

# Garante que deu certo
resposta.raise_for_status()

dados = resposta.json()
print(type(dados))
df = pd.DataFrame(dados)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())


#Convertendo textos para número
#df["idade"] = pd.to_numeric(df["idade"], errors="coerce") #errors="coerce" transforma valores inválidos em NaN.
#Convertendo texto para data
#df["data_cadastro"] = pd.to_datetime(df["data_cadastro"], errors="coerce")




usuario = {
    "id": 1,
    "nome": "Ana",
    "endereco": {
        "rua": "Rua A",
        "cidade": "Juiz de Fora",
        "estado": "MG"
    }
}

df = pd.DataFrame([usuario])
print(df)
from pandas import json_normalize
df = json_normalize(usuario)
print(df)




usuarios = [
    {
        "id": 1,
        "nome": "Ana",
        "endereco": {"cidade": "Juiz de Fora", "estado": "MG"}
    },
    {
        "id": 2,
        "nome": "Bruno",
        "endereco": {"cidade": "São Paulo", "estado": "SP"}
    }
]

df = json_normalize(usuarios)
print(df)

#Depois de carregar os dados, nem sempre queremos todas as colunas. Por exemplo, com o DataFrame acima:
df_simplificado = df[["nome", "endereco.cidade", "endereco.estado"]]
print(df_simplificado)
#Para renomear colunas:
df_simplificado = df_simplificado.rename(
    columns={
        "endereco.cidade": "cidade",
        "endereco.estado": "estado"
    }
)
print(df_simplificado)