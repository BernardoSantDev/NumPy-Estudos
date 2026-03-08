import pandas as pd
import numpy as np

data = {
    'A': [1,2,np.nan,4,5],
    'B': [np.nan,2,3,4,5],
    'C': [1,2,3,np.nan,np.nan]
}


df = pd.DataFrame(data)
print(df)


#selecionar a linha de indice 1
linha_1 = df.iloc[1]

#concatenar com duplicada
df_com_duplicata = pd.concat([df,linha_1.to_frame().T], ignore_index=True)
print(df_com_duplicata)

#eliminar duplicata
df_com_duplicata = df_com_duplicata.drop_duplicates()
print(df_com_duplicata)

#----------------------------------------------------------------------------

data = {
    'A': [1,6,np.nan,8,5],
    'B': [np.nan,6,3,4,5],
    'C': [1,8,3,np.nan,np.nan]
}

df = pd.DataFrame(data)
print(df)

#exercicio: df com notas de alunos em 3 diciplinas ABC a média é 6 nulo nao fez 4 reprovado 5 recuperação

def notas(nota):
    if pd.isna(nota):
        return 'Nao fez a prova'
    elif nota <= 4:
        return 'Reprovado'
    elif nota <= 6 and nota >= 5:
        return 'Recuperacao'
    else:
        return 'Aprovado'


df_com_notas = df.applymap(notas)
print(df_com_notas)


