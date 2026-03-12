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

#Cenario 4: Mais de 100 passageiros e distancia < 1000 milhas
p_distancia = df[(df['Passengers']>100) & (df['Distance']<1000)]
print(p_distancia)

#Cenario 5: todos voos de/para NY ou LA
cidades = df[df['Origin City'].str.contains('New York|Los Angeles') 
            |df['Destination City'].str.contains('New York|Los Angeles')]
print(cidades)

#Cenario 6: Pop origem superios a 1 milhao
origem = df[(df['Origin Population']>1_000_000)]
print(origem)


#Cenario 7: Voos com assentos vazios
voos = df.query('Seats > Passengers')
print(voos)
print(voos['Destination City'])


#Cenario 8: voos com dist > 300 e com mais de 10 voos por mes
voosp = df.query('Distance < 300 & Flights > 10')
print(voosp)