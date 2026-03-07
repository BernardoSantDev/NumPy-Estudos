import pandas as pd
import numpy as np

data = {
    'A': [1,2,np.nan,4,5],
    'B': [np.nan,2,3,4,5],
    'C': [1,2,3,np.nan,np.nan]
}


df = pd.DataFrame(data)
print(df)

print(df.isna())


#tira linha com valor ausente
removea = df.dropna()
print(removea)


#tira coluna com valor ausente
removec = df.dropna(axis=1)
print(removec)



#preenche valor nulo
preenche = df.fillna("N")
print(preenche)












