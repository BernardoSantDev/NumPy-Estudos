import pandas as pd
import numpy as np

students_ids = [n for n in range(200,225)]
p_mat = np.random.normal(70,10,25)
p_ing = np.random.normal(70,10,25)
p_hist = np.random.normal(70,10,25)

df = pd.DataFrame({
    'Student ID': students_ids,
    'Matematica': p_mat,
    'Ingles': p_ing,
    'Historia': p_hist
})


print(df['Matematica'])
print(df.head())
print(df.tail())
print(df.describe())


#classificando
sorted_df = df.sort_values(by='Matematica')
print(sorted_df)
print(sorted_df.tail())



#fatiamento (linhas de 5 a 10)
print(df.loc[5:10, ['Matematica']])
print(df.loc[5:10, ['Matematica', 'Ingles']])

#Filtrar condicional
notas_altas = df[df['Matematica'] > 75]
print(notas_altas)

notas_altas = df[(df['Matematica'] > 75) & (df['Ingles'] < 60)]
print(notas_altas)

#add ou remover coluna
df['Total'] = df['Matematica'] + df['Ingles'] + df['Historia']
print(df)

df.drop(columns='Total', inplace=True)
print(df)
















