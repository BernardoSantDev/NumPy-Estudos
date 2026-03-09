import pandas as pd
import numpy as np

data = {
    'Escola': ['A', 'B','A', 'B','A', 'B','A', 'B'],
    'Student ID': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    'Matematica': np.random.randint(60,100,8),
    'Ingles': np.random.randint(60,100,8),
    'Historia': np.random.randint(60,100,8)
}

df = pd.DataFrame(data)


# Add nova coluna
df['Turma'] = ['X', 'X', 'Y', 'Y','X', 'Y', 'Y', 'X',]

# Agrupando por multiplas colunas
grouped_multi = df.groupby(['Escola', 'Turma'])

#Calculando a media para o grupo multinivel
print(grouped_multi.mean())


print(df.groupby(['Escola', 'Turma']).mean())

sports_data = {
    'Student ID': [1001, 1002, 1003, 1004, 1005, 1006, 1009, 1010],
    'Esportes': ['Futebol', 'Basquete', 'Volei', 'Futebol', 'Volei', 'Futebol', 'Basquete', 'Volei']
}

sports_df = pd.DataFrame(sports_data)

#mesclando data frames | junção interna
merged_df = pd.merge(df, sports_df, on='Student ID')
print(merged_df)

#junção externa
merged_outer = pd.merge(df, sports_df, on='Student ID', how='outer')
print(merged_outer)
