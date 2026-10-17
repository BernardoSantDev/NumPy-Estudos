import pandas as pd

dados_imoveis = {
    "preco": [250000, 320000, 500000, 450000, 280000, 600000, 750000, 300000],
    "area_m2": [60, 80, 120, 100, 70, 150, 200, 75],
    "quartos": [2, 3, 3, 3, 2, 4, 4, 2],
    "banheiros": [1, 2, 2, 3, 1, 3, 3, 2],
    "vaga": [1, 1, 2, 2, 1, 3, 3, 1]
}

df_imoveis = pd.DataFrame(dados_imoveis)
print(df_imoveis)
print(df_imoveis.describe())
print(df_imoveis[["preco", "area_m2"]].describe())
media_preco = df_imoveis["preco"].mean()
mediana_preco = df_imoveis["preco"].median()
preco_maximo = df_imoveis["preco"].max()
preco_minimo = df_imoveis["preco"].min()
print("Preço médio:", media_preco)
print("Preço mediano:", mediana_preco)
print("Preço mínimo:", preco_minimo)
print("Preço máximo:", preco_maximo)

#Variância: medida da dispersão em relação à média.
#Desvio padrão: raiz quadrada da variância, na mesma unidade da variável.

desvio_preco = df_imoveis["preco"].std()
variancia_preco = df_imoveis["preco"].var()

print("Desvio padrão do preço:", desvio_preco)
print("Variância do preço:", variancia_preco)


print(df_imoveis[["preco", "area_m2"]].std())
print(df_imoveis[["preco", "area_m2"]].var())


#Correlação (aqui, correlação de Pearson) mede o grau de relação linear entre duas variáveis numéricas.
#Varia entre -1 e 1.
#Próximo de 1 → relação positiva forte.
#Quando uma aumenta, a outra tende a aumentar.
#Próximo de -1 → relação negativa forte.
#Quando uma aumenta, a outra tende a diminuir.
#Próximo de 0 → pouca ou nenhuma relação linear.


corr_imoveis = df_imoveis.corr(numeric_only=True)
print(corr_imoveis)


#Exemplo de interpretação (valores ilustrativos):
#preco x area_m2 → 0.92 (forte correlação positiva).
#preco x quartos → 0.85 (forte correlação positiva).
#area_m2 x quartos → 0.80.
#Nesse contexto, faz sentido: imóveis maiores tendem a ser mais caros e a ter mais quartos.
#“Existe uma forte correlação positiva entre área e preço, indicando que imóveis maiores tendem a ser mais caros.”


print("------------------------------------------------------------------------------------")

dados_estudo = {
    "horas_estudo": [1, 2, 3, 4, 5, 6, 7, 8],
    "nota_prova":   [4.0, 5.0, 5.5, 6.0, 7.0, 7.5, 8.0, 9.0]
}

df_estudo = pd.DataFrame(dados_estudo)
print(df_estudo)
print(df_estudo.describe())

corr_estudo = df_estudo.corr(numeric_only=True)
print(corr_estudo)

#“Há uma correlação positiva forte entre horas de estudo e nota, sugerindo que, neste conjunto de dados, alunos que estudam mais tendem a tirar notas mais altas.”


import matplotlib.pyplot as plt

plt.scatter(df_estudo["horas_estudo"], df_estudo["nota_prova"])
plt.xlabel("Horas de estudo")
plt.ylabel("Nota na prova")
plt.title("Relação entre horas de estudo e nota")
plt.show()









