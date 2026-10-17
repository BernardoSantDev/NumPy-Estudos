import pandas as pd


dados = {
    "renda": [
        1800, 2200, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000,
        6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 12000, 15000,
        2100, 2800, 3300, 3700, 4200, 4800, 5300, 5800, 6200, 6800,
        7300, 7800, 8200, 8700, 9200, 9800, 11000, 13000, 16000, 20000,
        1900, 2600, 3200, 3900, 4600, 5200, 6100, 7400, 8900, 14000
    ],

    "clicou_email": [
        0, 0, 1, 1, 0, 1, 1, 0, 1, 1,
        0, 1, 0, 1, 1, 1, 0, 1, 0, 1,
        0, 1, 1, 0, 1, 0, 1, 1, 0, 1,
        1, 0, 1, 0, 1, 1, 0, 1, 0, 1,
        0, 1, 0, 1, 0, 1, 1, 0, 1, 0
    ],

    "comprou": [
        0, 0, 1, 0, 0, 1, 1, 0, 1, 1,
        0, 1, 0, 1, 0, 1, 0, 1, 0, 1,
        0, 1, 0, 0, 1, 0, 1, 1, 0, 1,
        0, 0, 1, 0, 1, 1, 0, 1, 0, 1,
        0, 1, 0, 1, 0, 1, 0, 0, 1, 0
    ]
}


df = pd.DataFrame(dados)
print(df)

X = df[["renda", "clicou_email"]]
y = df["comprou"]

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

print("Tamanho treino:", len(x_train))
print("Tamanho teste:", len(x_test))

from sklearn.linear_model import LogisticRegression

modelo = LogisticRegression()
modelo.fit(x_train, y_train)


# Predição de classes (0 ou 1)
y_pred_classes = modelo.predict(x_test)
print("Classes preditas:", y_pred_classes.tolist())

# Probabilidades para cada classe
probas = modelo.predict_proba(x_test)
print("\nProbabilidades (coluna 0 = prob de NÃO comprar, coluna 1 = prob de comprar):\n", probas)

import numpy as np

probas_compra = probas[:, 1]  # segunda coluna = probabilidade de comprar
y_pred_0_5 = (probas_compra >= 0.5).astype(int)

print("Predição com limiar 0.5:", y_pred_0_5.tolist())

from sklearn.metrics import precision_score, recall_score

def avalia_limite(threshold):
    y_pred = (probas_compra >= threshold).astype(int)
    precisao = precision_score(y_test, y_pred, zero_division=0)
    recall   = recall_score(y_test, y_pred, zero_division=0)
    print(f"\nLimiar = {threshold}")
    print("Predições:", y_pred.tolist())
    print(f"Precisão: {precisao:.2f}")
    print(f"Recall:   {recall:.2f}")

for t in [0.3, 0.5, 0.7]:
    avalia_limite(t)

from sklearn.metrics import classification_report

# Usando o limiar padrão (0.5) via predict()
y_pred_default = modelo.predict(x_test)

print("Relatório com limiar padrão (0.5):\n")
print(classification_report(y_test, y_pred_default, zero_division=0))
























