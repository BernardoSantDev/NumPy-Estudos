import pandas as pd

dados = {
    "renda": [
        1800, 2500, 3200, 4500, 6000, 7500, 9000, 11000, 1400, 2800,
        3700, 5200, 6800, 8200, 10500, 12500, 1600, 2300, 4100, 5500,
        7200, 8800, 9800, 13500, 1900, 3000, 4800, 6300, 7900, 11500,
        1300, 2600, 3500, 5000, 6500, 8500, 10000, 14500, 2100, 3300,
        4300, 5700, 7000, 9200, 12000, 15000, 1700, 2900, 3900, 6100,
        1800, 2700, 3600, 4700, 6400, 7800, 9500, 11800, 1500, 3100,
        4400, 5900, 7300, 8900, 10800, 13800, 2000, 3400, 4900, 6700,
        8100, 9700, 11200, 14200, 1400, 2400, 3800, 5300, 6900, 8600,
        10300, 12800, 2200, 3000, 4200, 5600, 7400, 9100, 11600, 14800,
        1600, 2800, 4600, 6200, 7700, 9400, 10900, 13200, 1900, 3500
    ],

    "dividas": [
        1, 1, 1, 0, 0, 0, 0, 0, 1, 1,
        1, 0, 0, 0, 0, 0, 1, 1, 0, 1,
        0, 0, 1, 0, 1, 1, 0, 1, 0, 0,
        1, 1, 1, 0, 0, 0, 0, 0, 1, 1,
        0, 1, 0, 0, 0, 0, 1, 1, 1, 0,
        1, 1, 0, 1, 0, 0, 0, 0, 1, 1,
        0, 0, 0, 0, 0, 0, 1, 1, 0, 1,
        0, 0, 0, 0, 1, 1, 1, 0, 0, 0,
        0, 0, 1, 1, 0, 1, 0, 0, 0, 0,
        1, 1, 0, 1, 0, 0, 0, 0, 1, 1
    ],

    "idade": [
        21, 24, 29, 35, 42, 38, 45, 52, 19, 26,
        31, 33, 40, 47, 50, 58, 20, 23, 36, 28,
        41, 44, 55, 61, 22, 27, 34, 39, 46, 53,
        18, 25, 30, 37, 43, 49, 56, 63, 21, 29,
        32, 38, 45, 51, 59, 65, 19, 24, 35, 42,
        20, 26, 31, 36, 40, 48, 54, 62, 18, 28,
        33, 39, 44, 50, 57, 64, 22, 30, 37, 41,
        46, 52, 58, 60, 19, 25, 32, 38, 43, 49,
        55, 63, 23, 27, 34, 40, 47, 53, 59, 65,
        21, 29, 36, 42, 48, 54, 61, 64, 20, 31
    ],

    "risco": [
        1, 1, 1, 0, 0, 0, 0, 0, 1, 1,
        1, 0, 0, 0, 0, 0, 1, 1, 0, 1,
        0, 0, 0, 0, 1, 1, 0, 1, 0, 0,
        1, 1, 1, 0, 0, 0, 0, 0, 1, 1,
        0, 1, 0, 0, 0, 0, 1, 1, 1, 0,
        1, 1, 0, 1, 0, 0, 0, 0, 1, 1,
        0, 0, 0, 0, 0, 0, 1, 1, 0, 1,
        0, 0, 0, 0, 1, 1, 1, 0, 0, 0,
        0, 0, 1, 1, 0, 1, 0, 0, 0, 0,
        1, 1, 0, 1, 0, 0, 0, 0, 1, 1
    ]
}

df = pd.DataFrame(dados)
print(df)

from sklearn.model_selection import train_test_split

X = df[["renda", "dividas", "idade"]]
y = df["risco"]

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y,
    test_size=0.25,      # 25% para teste
    random_state=42
)

print("Tamanho treino:", len(X_treino))
print("Tamanho teste:", len(X_teste))

from sklearn.tree import DecisionTreeClassifier

arvore = DecisionTreeClassifier(
    max_depth=3,        # profundidade máxima da árvore
    random_state=42
)

arvore.fit(X_treino, y_treino)

from sklearn.metrics import classification_report, confusion_matrix

y_pred = arvore.predict(X_teste)

print("Matriz de confusão:\n", confusion_matrix(y_teste, y_pred))
print("\nRelatório de classificação:\n", classification_report(y_teste, y_pred, zero_division=0))

print("Acurácia treino:", arvore.score(X_treino, y_treino))
print("Acurácia teste:",  arvore.score(X_teste, y_teste))

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

plt.figure(figsize=(10, 6))
plot_tree(
    arvore,
    feature_names=X.columns,
    class_names=["baixo", "alto"],
    filled=True,
    rounded=True
)
plt.show()


arvore_profunda = DecisionTreeClassifier(
    random_state=42  # sem max_depth
)

arvore_profunda.fit(X_treino, y_treino)

print("Acurácia treino (profunda):", arvore_profunda.score(X_treino, y_treino))
print("Acurácia teste  (profunda):", arvore_profunda.score(X_teste, y_teste))