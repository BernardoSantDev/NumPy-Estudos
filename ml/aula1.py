from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


#CLASSIFICAÇÃO
iris = load_iris()

X = iris.data
y = iris.target

print("Formato de X (linhas, colunas):", X.shape)
print("Formato de y (linhas):", y.shape)
print("Primeiras 5 linhas de X:\n", X[:5])
print("Primeiras 5 linhas de y:\n", y[:5])
print("Nomes das classes:", iris.target_names)
print("Nomes das features:", iris.feature_names)

x_treino, x_teste, y_treino, y_teste = train_test_split(
    X, y,
    test_size=0.2,    #20% dos dados para teste
    random_state=42   #"semente" para resultados reproduzíveis
)

print("Tamanho treino:", x_treino.shape[0])
print("Tamanho teste:", x_teste.shape[0])


modelo = DecisionTreeClassifier()
modelo.fit(x_treino, y_treino)

acuracia_treino = modelo.score(x_treino, y_treino)
acuracia_teste = modelo.score(x_teste, y_teste)
print(f"Acurácia no treino: {acuracia_treino:.2f}")
print(f"Acurácia no teste:  {acuracia_teste:.2f}")


import numpy as np

# Pega a primeira linha de X_teste
exemplo = x_teste[0].reshape(1, -1)
print("Medidas da flor de exemplo:", exemplo)

predicao = modelo.predict(exemplo)
print("Classe predita (número):", predicao)
print("Classe predita (nome):", iris.target_names[predicao][0])

# Valor real:
print("Classe real (número):", y_teste[0])
print("Classe real (nome):", iris.target_names[y_teste[0]])


#--------------------------------------------------------------------------------------------------------

#REGRESSÃO

import numpy as np
from sklearn.linear_model import LinearRegression

# Horas de estudo (X) e notas (y)
horas = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)  # 6 alunos - esse será nosso conjunto de dados de entrada (X) - o uso do reshape é para transformar o array em uma matriz de 6 linhas e 1 coluna, que é o formato esperado pelo modelo
notas = np.array([4, 5, 6, 7, 8, 9])                 # nota ficticia - esse será nosso conjunto de dados de saída (y) - nao usamos reshape aqui porque o modelo espera um array unidimensional para a saída
print(horas)

modelo_reg = LinearRegression()
modelo_reg.fit(horas, notas)

# Prever nota de alguém que estudou 3.5 horas
nova_hora = np.array([[3.5]])
nota_prevista = modelo_reg.predict(nova_hora)
print(f"Nota prevista para 3.5 horas de estudo: {nota_prevista[0]:.2f}")


#------------------------------------------------------------------------------------

#Atividade 

import pandas as pd

dados = {
    "horas_estudo": [1, 3, 5, 2, 7, 4, 6, 8, 2, 5, 9, 3, 6, 4, 10],
    "assistiu_aulas": [0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    "aprovado": [0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1]
}

data_dados = pd.DataFrame(dados)

x = data_dados[["horas_estudo", "assistiu_aulas"]]
y = data_dados["aprovado"]

x_treino, x_teste, y_treino, y_teste = train_test_split(
    x, y,
    test_size=0.2,
    random_state=42
)

modelo_atividade = DecisionTreeClassifier()
modelo_atividade.fit(x_treino, y_treino)

acuracia_treino_atividade = modelo_atividade.score(x_treino, y_treino)
acuracia_teste_atividade = modelo_atividade.score(x_teste, y_teste)
print(f"Acurácia no treino (atividade): {acuracia_treino_atividade:.2f}")
print(f"Acurácia no teste (atividade):  {acuracia_teste_atividade:.2f}")



