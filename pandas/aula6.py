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

#Agrupando
agrupa = df.groupby('Escola')
print(agrupa)

# Agregando
m_escola = agrupa.mean()
print(m_escola)

#aplicando multiplas operaçoes
agg_data = agrupa.agg({
    'Matematica': ['mean', 'median', 'std']
})
print(agg_data)



