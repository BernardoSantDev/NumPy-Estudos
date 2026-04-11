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

#Usando pandas.read_json direto
import pandas as pd

df_vendas = pd.read_json("vendas.json")
print(df_vendas)
print(df_vendas.info())
#Você também pode ler JSON de string:

json_string = '[{"id": 1, "nome": "Ana"}, {"id": 2, "nome": "Bruno"}]'
df = pd.read_json(json_string)