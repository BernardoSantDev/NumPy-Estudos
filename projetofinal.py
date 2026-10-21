import os
os.environ["LOKY_MAX_CPU_COUNT"] = "4" 
import sys; sys.stdout.reconfigure(encoding="utf-8")

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



#DEFININDO MODELOS
from sklearn.compose import ColumnTransformer
# Separamos colunas numéricas e (opcional) categóricas
colunas_numericas = X_treino.select_dtypes(include=[np.number]).columns.tolist()
colunas_categoricas = X_treino.select_dtypes(exclude=[np.number]).columns.tolist()
# Para simplificar, vamos:
# - escalonar apenas as numéricas
# - transformar categóricas com one-hot encoding (se houver)
from sklearn.preprocessing import OneHotEncoder
preprocessador = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), colunas_numericas),
        ("cat", OneHotEncoder(handle_unknown="ignore"), colunas_categoricas)
    ]
)
modelos = {
    "LogisticRegression": LogisticRegression(max_iter=500),
    "RandomForest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ),
    "KNN": KNeighborsClassifier(n_neighbors=5)
}
from sklearn.pipeline import Pipeline
pipelines = {}
for nome, modelo in modelos.items():
    pipelines[nome] = Pipeline(steps=[
        ("preprocessamento", preprocessador),
        ("modelo", modelo)
    ])


#TREINO E AVALIAÇÃO DE CADA MODELO
resultados = []
for nome, pipe in pipelines.items():
    print(f"\nTreinando modelo: {nome}")
    pipe.fit(X_treino, y_treino)

    y_pred = pipe.predict(X_teste)

    acc  = accuracy_score(y_teste, y_pred)
    prec = precision_score(y_teste, y_pred, zero_division=0)
    rec  = recall_score(y_teste, y_pred, zero_division=0)
    f1   = f1_score(y_teste, y_pred, zero_division=0)

    resultados.append({
        "modelo": nome,
        "accuracy": acc,
        "precision": prec,
        "recall": rec,
        "f1": f1
    })

    print(f"Acurácia:  {acc:.3f}")
    print(f"Precisão:  {prec:.3f}")
    print(f"Recall:    {rec:.3f}")
    print(f"F1-score:  {f1:.3f}")

resultado_df = pd.DataFrame(resultados)
print("\nResumo dos modelos:\n")
print(resultado_df)




#INSPECIONA O MELHOR MNODELO EM MAIS DETALHES
melhor_nome = resultado_df.sort_values("f1", ascending=False).iloc[0]["modelo"]
print(f"\nMelhor modelo (pelo F1): {melhor_nome}")
melhor_pipeline = pipelines[melhor_nome]
y_pred_melhor = melhor_pipeline.predict(X_teste)
print("\nMatriz de confusão:")
print(confusion_matrix(y_teste, y_pred_melhor))
print("\nRelatório de classificação:")
print(classification_report(y_teste, y_pred_melhor,zero_division=0))
if melhor_nome == "RandomForest":
    # Pegando o modelo interno já treinado:
    modelo_rf = melhor_pipeline.named_steps["modelo"]

    # Nome das colunas após o preprocessamento (num + one-hot)
    # Para simplificar, vamos mostrar apenas importâncias totais,
    # mas em produção você mapeia as colunas transformadas.
    importancias = modelo_rf.feature_importances_
    print("\nNúmero de features após transformações:", len(importancias))
if melhor_nome == "RandomForest" and len(colunas_categoricas) == 0:
    importancias_df = pd.DataFrame({
        "feature": colunas_numericas,
        "importancia": modelo_rf.feature_importances_
    }).sort_values("importancia", ascending=False)

    print("\nImportância das variáveis (aprox.):")
    print(importancias_df)




#VE A IMPORTANCIA DAS COLUNAS
modelo_rf = melhor_pipeline.named_steps["modelo"]
nomes = melhor_pipeline.named_steps["preprocessamento"].get_feature_names_out()
imp = pd.DataFrame({"feature": nomes, "importancia": modelo_rf.feature_importances_})
# tira o prefixo num__/cat__ e junta o one-hot na variável original
imp["variavel"] = imp["feature"].str.replace(r"^(num|cat)__", "", regex=True)
for c in colunas_categoricas:
    imp.loc[imp["variavel"].str.startswith(c + "_"), "variavel"] = c
print(imp.groupby("variavel")["importancia"].sum().sort_values(ascending=False).round(3))
# direção do efeito: média de cada variável por grupo
print(
    df.groupby("churn")[["nota_satisfacao", "uso_mensal_horas", "qtd_chamados_suporte",
                         "meses_como_cliente", "atrasos_pagamento_12m"]]
      .mean().round(2).T
)

# ============================================================
# 7. MINI RELATÓRIO PARA A GESTÃO
# ============================================================
#
# Testamos três modelos (Regressão Logística, Random Forest e KNN) para
# prever cancelamento de clientes a partir de perfil, uso e atendimento.
# O melhor F1 foi o da Random Forest (0,68), com acurácia de 0,84,
# precisão de 0,76 e recall de 0,62.
#
# Na prática, o modelo identifica cerca de 62% dos clientes que de fato
# cancelam (34 de 55 no teste) e, quando sinaliza um cancelamento, acerta
# em 76% das vezes.
#
# As variáveis mais importantes foram a nota de satisfação, o uso mensal,
# a quantidade de chamados ao suporte e o tempo como cliente: quem
# cancela tem notas menores, usa menos o serviço, procura mais o suporte
# e é cliente há menos tempo.
#
# Sugerimos gerar semanalmente uma lista de clientes com alta
# probabilidade de cancelar e priorizar ações de retenção (contato
# proativo, ofertas) para quem tem nota baixa e muitos chamados.
#
# Como limitação, a base é simulada e o modelo ainda deixa escapar cerca
# de 4 em cada 10 cancelamentos.
