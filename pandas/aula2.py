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



















