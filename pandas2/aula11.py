import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dados_imoveis = {
    "preco": [250000, 320000, 500000, 450000, 280000, 600000, 750000, 300000],
    "area_m2": [60, 80, 120, 100, 70, 150, 200, 75]
}

df_imoveis = pd.DataFrame(dados_imoveis)
print(df_imoveis)


#x = area_m2
#y = preco
#numpy.polyfit recebe:
#x = array com valores da variável independente.
#y = array com valores da variável dependente.
#deg = grau do polinômio. Para reta, deg = 1.
#Ele devolve os coeficientes do polinômio. No caso linear:
#coef[0] = a (inclinação)
#coef[1] = b (intercepto)

x = df_imoveis["area_m2"]
y = df_imoveis["preco"]

coef = np.polyfit(x, y, deg=1)
print(coef)

a = coef[0]
b = coef[1]

print(f"Coeficiente angular (a): {a}")
print(f"Coeficiente linear (b): {b}")


df_imoveis["preco_previsto"] = a * df_imoveis["area_m2"] + b
print(df_imoveis)


df_imoveis["erro"] = df_imoveis["preco"] - df_imoveis["preco_previsto"]
print(df_imoveis[["area_m2", "preco", "preco_previsto", "erro"]])

plt.scatter(df_imoveis["area_m2"], df_imoveis["preco"], label="Dados reais")
plt.plot(df_imoveis["area_m2"], df_imoveis["preco_previsto"], color="red", label="Reta ajustada")
plt.xlabel("Área (m²)")
plt.ylabel("Preço (R$)")
plt.title("Regressão linear: preço x área")
plt.legend()
plt.show()


def prever_preco(area_m2):
    return a * area_m2 + b

print(prever_preco(90))
print(prever_preco(130))














































