#Lendo JSON e XML de Arquivos Locais e Integrando Múltiplas Fontes


#Usando json (para ter controle total)
import json

with open("vendas.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

print(type(dados))  # deve ser list
print(dados)
import pandas as pd

df_vendas = pd.DataFrame(dados)
print(df_vendas)