import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Dados fictícios de churn
dados = {
    "meses_como_cliente": [2, 12, 24, 36, 5, 8, 18, 30, 4, 40],
    "chamados_suporte":   [5,  1,  0,  2, 6, 3,  1,  0, 7,  0],
    "plano_premium":      [0,  1,  1,  1, 0, 0,  1,  1, 0,  1],
    "churn":              [1,  0,  0,  0, 1, 1,  0,  0, 1,  0]
}

df = pd.DataFrame(dados)

X = df[["meses_como_cliente", "chamados_suporte", "plano_premium"]]
y = df["churn"]

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y,
    test_size=0.5,
    random_state=42
)

modelo = LogisticRegression()
modelo.fit(X_treino, y_treino)


from sklearn.metrics import confusion_matrix

y_pred = modelo.predict(X_teste)
matriz = confusion_matrix(y_teste, y_pred)
print("Matriz de Confusão:")
print(matriz)

#TN (True Negative) → era 0 e o modelo previu 0 (acerto).
#TP (True Positive) → era 1 e o modelo previu 1 (acerto).
#FP (False Positive) → era 0 e o modelo previu 1 (falso alarme).
#FN (False Negative) → era 1 e o modelo previu 0 (deixou passar algo importante).
#Alguns exemplos:
#Em churn:
#FP: o modelo acha que o cliente vai sair, mas ele ficaria.
#FN: o modelo acha que o cliente vai ficar, mas ele sai (perigo!).
#Em detecção de doença:
#FP: dizer que a pessoa tem doença, mas ela não tem.
#FN: dizer que a pessoa não tem doença, mas ela tem (muito grave).
#[[TN  FP]
# [FN  TP]]

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)


print("Acurácia:",  accuracy_score(y_teste, y_pred))
print("Precisão:",  precision_score(y_teste, y_pred, zero_division=0))
print("Recall:",    recall_score(y_teste, y_pred, zero_division=0))
print("F1-score:",  f1_score(y_teste, y_pred, zero_division=0))

print("\nRelatório completo:\n")
print(classification_report(y_teste, y_pred, zero_division=0))


#Precision (Precisão): entre as previsões feitas para uma classe, quantas estavam corretas.
#Recall (Revocação): entre os casos reais de uma classe, quantos o modelo conseguiu identificar.
#F1-score: equilíbrio entre precisão e recall.
#Support: quantidade de exemplos reais de cada classe utilizados no teste.

#---------------------------------------------------------------------------------------------------------


dados2 = {
    "meses_como_cliente": [
        2, 12, 24, 36, 5, 8, 18, 30, 4, 40,
        15, 22, 28, 32, 10, 14, 20, 26, 38, 45,
        6, 16, 25, 34, 42, 11, 19, 29, 37, 48,
        7, 13, 21, 27, 33, 39, 44, 50, 52, 55,
        9, 17, 23, 31, 35, 41, 46, 49, 53, 58,
        3, 18, 24, 30, 36, 43, 47, 51, 56, 60,
        14, 20, 26, 32, 38, 45, 54, 57, 59, 28,
        12, 16, 22, 34, 40, 48, 52, 55, 58, 60,
        19, 25, 31, 37, 42
    ],

    "chamados_suporte": [
        5, 1, 0, 2, 6, 3, 1, 0, 7, 0,
        2, 1, 0, 1, 2, 1, 0, 1, 0, 0,
        2, 1, 0, 1, 0, 2, 1, 0, 1, 0,
        1, 2, 1, 0, 1, 0, 2, 0, 1, 0,
        3, 1, 0, 2, 1, 0, 1, 0, 2, 0,
        4, 1, 0, 2, 1, 0, 1, 0, 2, 0,
        1, 0, 2, 1, 0, 1, 0, 2, 0, 1,
        2, 0, 1, 0, 2, 1, 0, 1, 0, 2,
        1, 0, 2, 1, 0
    ],

    "plano_premium": [
        0, 1, 1, 1, 0, 0, 1, 1, 0, 1,
        1, 1, 1, 1, 0, 1, 1, 1, 1, 1,
        0, 1, 1, 1, 1, 0, 1, 1, 1, 1,
        0, 1, 1, 0, 1, 1, 0, 1, 1, 1,
        0, 1, 0, 1, 1, 1, 0, 1, 1, 1,
        0, 1, 1, 1, 1, 0, 1, 1, 1, 1,
        1, 0, 1, 1, 1, 1, 1, 0, 1, 1,
        1, 0, 1, 1, 1, 0, 1, 1, 0, 1,
        1, 1, 0, 1, 1
    ],

    "churn": [
        1, 0, 0, 0, 1, 1, 0, 0, 1, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0
    ]
}

df = pd.DataFrame(dados2)

X = df[["meses_como_cliente", "chamados_suporte", "plano_premium"]]
y = df["churn"]

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y,
    test_size=0.4,
    random_state=42
)

modelo = LogisticRegression()
modelo.fit(X_treino, y_treino)

from sklearn.metrics import confusion_matrix

y_pred = modelo.predict(X_teste)
matriz = confusion_matrix(y_teste, y_pred)
print("Matriz de Confusão:")
print(matriz)


print("Acurácia:",  accuracy_score(y_teste, y_pred))
print("Precisão:",  precision_score(y_teste, y_pred, zero_division=0))
print("Recall:",    recall_score(y_teste, y_pred, zero_division=0))
print("F1-score:",  f1_score(y_teste, y_pred, zero_division=0))

print("\nRelatório completo:\n")
print(classification_report(y_teste, y_pred, zero_division=0))








