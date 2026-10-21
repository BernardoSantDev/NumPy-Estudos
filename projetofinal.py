import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)




#CARREGANDO DADOS
df = pd.read_csv("clientes_churn.csv")
print("Primeiras linhas:")
print(df.head())
print("Informações do DataFrame:")
print(df.info())    
print("Estatísticas descritivas:")
print(df.describe())

print(df.isna().sum())
if df["renda"].isna().sum() > 0:
    df["renda"] = df["renda"].fillna(df["renda"].median())
print("Ausentes em renda depois:", df["renda"].isna().sum()) 


#SEPARANDO FEATURES
y = df["churn"]
X = df.drop("churn", axis=1)

coluna_descartar = ['id_cliente']
X = X.drop(columns=[c for c in coluna_descartar if c in X.columns])
print(X.columns.tolist())



#SEPARANDO TREINO E TESTE
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y            # manter proporção de classes (se possível)
)

print("Tamanho treino: ", X_treino.shape)
print("Tamanho teste: ", X_teste.shape)





