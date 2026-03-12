import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('flights.csv')
print(df.head(10))
print(df.info())
print(df.isnull().sum())
print(df.describe().round(2))
print(df['Origin'].value_counts().head(10))

#unique() - util para identificar todos os valores sistindos em uma coluna de dados
#nunique() util para calcular a cardinalidade de um conjunto de dados, ou seja, quantos valores distintos existem
print(df['Origin'].unique())
print(df['Origin'].nunique())


#Cenario 1: extrair registros de voos apenas no ano 2000
df['Year'] = df['Fly Date'].astype(str).str.slice(0,4)
voos200 = df[df['Year'] == '2000']
print(voos200)

#Cenario 2: encontre voos que nao incluam LAX como origem
nox_lax = df[~df['Origin'].isin(['LAX'])]
print(nox_lax)


#Cenario 3: encontre voos que  incluam LAX como origem
lax = df[df['Origin'].isin(['LAX'])]
print(lax)





