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
resposta.rayse_for_status()
dados = resposta.json()
