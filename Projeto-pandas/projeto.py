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
