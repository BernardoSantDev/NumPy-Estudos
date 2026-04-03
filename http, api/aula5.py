import pandas as pd
from pandas import json_normalize
import requests
import numpy as np

dados = [
    {"id": 1, "cliente": " Ana ", "valor": "250.0", "data": "2025-11-01", "estado": "mg"},
    {"id": 2, "cliente": "Bruno", "valor": "300",   "data": "2025/11/02", "estado": "SP"},
    {"id": 3, "cliente": "Carla", "valor": None,    "data": "2025-11-03", "estado": "rj"},
    {"id": 4, "cliente": "Ana",   "valor": "abc",   "data": None,         "estado": "MG"},
    {"id": 4, "cliente": "Ana",   "valor": "abc",   "data": None,         "estado": "MG"}  # duplicado
]

df = pd.DataFrame(dados)
print(df)

#Encontrando valores ausentes
print(df.isna())          # mostra True/False por célula
print(df.isna().sum())    # mostra quantos NaN por coluna

#EXTRATÉGIAS
#remover linhas com valores ausentes
df_semNA = df.dropna()
print(df_semNA)
#Preencher valores ausentes com valor padrão
df_preenchido = df.fillna(0)
print(df_preenchido)

#CORRIGINDO TIPOS DE DADOS
#Colunas numéricas como texto → pd.to_numeric
#Na nossa tabela, valor é texto (object) e ainda por cima com alguns valores inválidos. Corrigindo
#errors="coerce": Se o valor não puder virar número (ex: "abc"), vira NaN.
df["valor"] = pd.to_numeric(df["valor"], errors="coerce")
print(df["valor"])
print(df.dtypes)

#Datas como texto → pd.to_datetime
#errors="coerce" transforma datas malformadas ou None em NaT (Not a Time – equivalente a NaN para datas).
df["data"] = pd.to_datetime(df["data"], errors="coerce")
print(df["data"])
print(df.dtypes)

#Limpando textos (strings)

#Removendo espaços extras
#str.strip() remove espaços no início e no fim.
df["cliente"] = df["cliente"].str.strip()
print(df["cliente"])

#Padronizando maiúsculas/minúsculas
#Você também poderia usar str.lower() para tudo minúsculo.
df["estado"] = df["estado"].str.upper()  # tudo maiúsculo
print(df["estado"])

#Outros métodos úteis
#str.replace("antigo", "novo")
#str.contains("texto") → para filtros
#str.len() → tamanho do texto
#Exemplo: filtrar clientes cujo nome começa com “A”:
print(df[df["cliente"].str.startswith("A")])


#Removendo duplicatas
print(df.duplicated())          # mostra True/False
print(df.duplicated().sum())    # quantas linhas duplicadas
df_sem_dup = df.drop_duplicates()
print(df_sem_dup)

#Criando colunas derivadas (Pandas + Numpy)
df["valor_com_desconto"] = df["valor"] * 0.9  # 10% de desconto
#Criando faixas com np.where
condicoes = [
    df["valor"] < 200,
    (df["valor"] >= 200) & (df["valor"] < 500),
    df["valor"] >= 500
]

valores = ["Baixo", "Médio", "Alto"]

df["faixa_valor"] = np.select(condicoes, valores, default="Desconhecido")
print(df[["valor", "faixa_valor"]])
print(df)