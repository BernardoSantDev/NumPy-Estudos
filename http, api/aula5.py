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