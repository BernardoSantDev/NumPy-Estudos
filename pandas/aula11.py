import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#data com nota
grades_data = {
    'Materias': ['Matematica', 'Portugues', 'Historia', 'Geografia', 'Fisica'],
    'Notas': [80,70,50,60,90]
}

grades_df = pd.DataFrame(grades_data)
grades_df.plot(kind='bar', x='Materias', y='Notas', color='blue')
plt.ylabel('Notas')
plt.tight_layout()
plt.show()




#crie um intervalo de datas para um ano
dates_rng = pd.date_range(start='1/1/2023', end='12/31/2023', freq='D')

#Gerando flutuações aleatorias em torno do preço inicial da ação
stock_data = 100 + np.cumsum(np.random.randn(365)*2)


#Criando dataframe
df = pd.DataFrame(stock_data, index=dates_rng, columns=['Preco'])
print(df)


df.plot(title='Preço das açoes ao longo do tempo')
plt.xlabel('Data')
plt.ylabel('Preco')
plt.tight_layout()
plt.show()

#histograma
































