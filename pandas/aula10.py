import pandas as pd
import numpy as np


#crie um intervalo de datas para um ano
dates_rng = pd.date_range(start='1/1/2018', end='12/31/2018', freq='D')

#Gerando flutuações aleatorias em torno do preço inicial da ação
stock_data = 100 + np.cumsum(np.random.randn(365)*2)


#Criando dataframe
df = pd.DataFrame(stock_data, index=dates_rng, columns=['Preco'])
print(df)

#faça uma amostra media mensal
mensal = df.resample('M').mean()
print(mensal)

#mude os dados de 1 dia
df_shifted = df.shift(1)

#preço dia seguinte
df['Preco no dia seguinte'] = df['Preco'].shift(1)

#variação diaria do preço
df['Mudanca diaria'] = df['Preco no dia seguinte'] - df['Preco']
print(df)


#calcule a media movel de 7 dias
df_rolling = df.rolling(window=7).mean()
print(df_rolling)




























