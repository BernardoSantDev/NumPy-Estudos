import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("insights de dados e clusters/clientes_ecommerce.csv")

#Para um primeiro clustering de comportamento de compras, talvez façam sentido:
#qtd_pedidos
#ticket_medio
#tempo_como_cliente_meses
#Colunas menos úteis para o primeiro momento:
#id_cliente → identificador, não indica comportamento.
#cidade → pode até ser útil, mas mistura geografia com comportamento (deixa pra depois).
#usa_cupom_desconto → poderia ser usada em outro experimento, mas por enquanto podemos simplificar.

features = ["qtd_pedidos", "ticket_medio", "tempo_como_cliente_meses"]
X = df[features]
print(X.head())

print(X.isna().sum())
#Remover linhas com valores ausentes (se forem poucas):
#X_clean = X.dropna()
#Preencher com um valor (ex.: média ou mediana):
#from sklearn.impute import SimpleImputer
#imputer = SimpleImputer(strategy="median")
#X_imputed = imputer.fit_transform(X)
#Para o curso, podemos usar a abordagem mais simples: dropar NaN quando a perda de dados não for grande.
print("Antes:", X.shape)
X = X.dropna()
print("Depois:", X.shape)

#O StandardScaler transforma cada coluna para ter:
#média ≈ 0
#desvio padrão ≈ 1
#Ou seja, deixa tudo em uma escala “comparável”.

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled) 

#fit_transform:
#fit aprende a média e o desvio de cada coluna.
#transform aplica a transformação aos dados.
#Depois disso, X_scaled é um array NumPy com os dados padronizados, pronto para ser usado em K-Means, DBSCAN, HAC etc.




