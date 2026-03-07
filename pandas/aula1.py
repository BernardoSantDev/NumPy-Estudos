import pandas as pd
import numpy as np

#Gerando dados aleatorios usando numpy
data_series = np.random.normal(0,1,100)
#converter array numpy em serie panda
p_series = pd.Series(data_series)

#imprime os primeiros 5 elementos
print(p_series.head())
#imprime os ultimos 5 elementos
print(p_series.tail())

# gerara outra sequencia
data_series2 = np.random.normal(0,1,100)

#criar um dicionario da series

frame = {
    'coluna1': data_series,
    'coluna2': data_series2
    }
#convertendo em dataframe
df = pd.DataFrame(frame)
print(df)


#descreve o dataframe
print(df.describe())

#falao valor menor e maior
print(df.sort_values(by = 'coluna1'))

#add coluna
df['Total'] = df['coluna1'] + df['coluna2']
print(df)

#remove coluna
df.drop(columns='Total', inplace=True)
print(df)




