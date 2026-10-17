from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import os
os.environ["LOKY_MAX_CPU_COUNT"] = "4"

iris = load_iris()
X = iris.data         # features (medidas das flores)
y = iris.target       # espécies (0, 1, 2)

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score


knn = Pipeline(steps=[
    ("scaler", StandardScaler()),             # 1) normaliza os dados
    ("modelo", KNeighborsClassifier(n_neighbors=5))  # 2) aplica o KNN
])

knn.fit(X_treino, y_treino)

y_pred = knn.predict(X_teste)
acc = accuracy_score(y_teste, y_pred)
print(f"Acurácia com K=5: {acc:.2f}")




resultados = []

for k in range(1, 16):  # K de 1 até 15
    knn_k = Pipeline(steps=[
        ("scaler", StandardScaler()),
        ("modelo", KNeighborsClassifier(n_neighbors=k))
    ])
    knn_k.fit(X_treino, y_treino)
    y_pred_k = knn_k.predict(X_teste)
    acc_k = accuracy_score(y_teste, y_pred_k)
    resultados.append((k, acc_k))

for k, acc_k in resultados:
    print(f"K = {k:2d} -> Acurácia: {acc_k:.2f}")


knn_sem_scaler = KNeighborsClassifier(n_neighbors=5)
knn_sem_scaler.fit(X_treino, y_treino)

y_pred_sem = knn_sem_scaler.predict(X_teste)
acc_sem = accuracy_score(y_teste, y_pred_sem)
print(f"Acurácia SEM scaler (K=5): {acc_sem:.2f}")


knn_com_scaler = Pipeline(steps=[
    ("scaler", StandardScaler()),
    ("modelo", KNeighborsClassifier(n_neighbors=5))
])
knn_com_scaler.fit(X_treino, y_treino)

y_pred_com = knn_com_scaler.predict(X_teste)
acc_com = accuracy_score(y_teste, y_pred_com)
print(f"Acurácia COM scaler (K=5): {acc_com:.2f}")

# É bem comum o modelo com scaler se sair igual ou melhor, especialmente quando as features estão em escalas muito diferentes.


import pandas as pd

dados_clientes = {
    "renda":           [2000, 3500, 5000, 8000, 12000, 3000, 4500, 9000, 7000, 15000],
    "idade":           [22,   25,   30,   35,   40,    24,   28,   38,   32,   45],
    "pontuacao_site":  [10,   40,   60,   80,   90,    20,   50,   85,   70,   95],
    "cliente_valioso": [0,    0,    0,    1,    1,     0,    0,    1,    1,    1]
}

df_cli = pd.DataFrame(dados_clientes)
print(df_cli)


from sklearn.model_selection import train_test_split

X_cli = df_cli[["renda", "idade", "pontuacao_site"]]
y_cli = df_cli["cliente_valioso"]

Xc_treino, Xc_teste, yc_treino, yc_teste = train_test_split(
    X_cli, y_cli,
    test_size=0.3,
    random_state=42
)

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

knn_cli = Pipeline(steps=[
    ("scaler", StandardScaler()),
    ("modelo", KNeighborsClassifier(n_neighbors=3))
])

knn_cli.fit(Xc_treino, yc_treino)
yc_pred = knn_cli.predict(Xc_teste)

print("Relatório de classificação (clientes):\n")
print(classification_report(yc_teste, yc_pred, zero_division=0))









