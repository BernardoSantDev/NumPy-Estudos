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











