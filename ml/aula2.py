import pandas as pd

# Dados fictícios de churn
dados = {
    "meses_como_cliente": [2, 12, 24, 36, 5, 8, 18, 30, 4, 40],
    "chamados_suporte":   [5,  1,  0,  2, 6, 3,  1,  0, 7,  0],
    "plano_premium":      [0,  1,  1,  1, 0, 0,  1,  1, 0,  1],
    "churn":              [1,  0,  0,  0, 1, 1,  0,  0, 1,  0]
}

df = pd.DataFrame(dados)
print(df)

X = df[["meses_como_cliente", "chamados_suporte", "plano_premium"]]  # entradas
y = df["churn"] # saída

from sklearn.model_selection import train_test_split

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y,
    test_size=0.3,      # 30% para teste
    random_state=42
)

print("Tamanho treino:", len(X_treino))
print("Tamanho teste:", len(X_teste))

from sklearn.linear_model import LogisticRegression

modelo = LogisticRegression()
modelo.fit(X_treino, y_treino)

print("Acurácia treino:", modelo.score(X_treino, y_treino))
print("Acurácia teste:",  modelo.score(X_teste, y_teste))



