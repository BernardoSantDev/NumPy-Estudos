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




