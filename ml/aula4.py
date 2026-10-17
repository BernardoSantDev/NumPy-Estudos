import pandas as pd
from sklearn.datasets import fetch_california_housing

dados = fetch_california_housing(as_frame=True)
df = dados.frame

print(df.head())
print("\nColunas disponíveis:\n", df.columns)
print(df.shape)

X = df.drop("MedHouseVal", axis=1)
y = df["MedHouseVal"]

from sklearn.model_selection import train_test_split

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print("\nTamanho do conjunto de treino:", X_treino.shape)
print("Tamanho do conjunto de teste:", X_teste.shape)


from sklearn.linear_model import LinearRegression

modelo = LinearRegression()
modelo.fit(X_treino, y_treino)


# MAE – Mean Absolute Error (Erro Médio Absoluto) - Em média, o quanto o modelo erra, em valor absoluto.
# MSE – Mean Squared Error (Erro Quadrático Médio) - Ele penaliza mais os erros grandes (porque é ao quadrado).
# RMSE – Root Mean Squared Error (Raiz do MSE) - Volta para a mesma unidade da variável alvo (tipo o MAE), mas ainda penaliza mais os erros grandes.
# R² – Coeficiente de determinação - Quanto da variação dos dados o modelo consegue explicar?


import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Fazer previsões no conjunto de teste
y_pred = modelo.predict(X_teste)

# 2. Calcular as métricas
mae = mean_absolute_error(y_teste, y_pred)
mse = mean_squared_error(y_teste, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_teste, y_pred)

print(f"MAE:  {mae:.3f}")
print(f"MSE:  {mse:.3f}")
print(f"RMSE: {rmse:.3f}")
print(f"R²:   {r2:.3f}")


#Um jeito visual de avaliar um modelo de regressão é: Comparar o valor real (y_teste) com o valor previsto (y_pred) em um gráfico de dispersão.

import matplotlib.pyplot as plt

plt.figure(figsize=(60, 100))
plt.scatter(y_teste, y_pred, alpha=0.5)
plt.xlabel("Valor real (y_teste)")
plt.ylabel("Valor previsto (y_pred)")
plt.title("Valores Reais vs Previstos – Preço de Casas")
plt.plot([y_teste.min(), y_teste.max()],
         [y_teste.min(), y_teste.max()],
         linestyle="--")  # linha ideal
plt.show()