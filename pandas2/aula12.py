import pandas as pd
import matplotlib.pyplot as plt

#df = ...  # seu DataFrame
#df.plot(kind="line")  # ou "bar", "hist", "box", "scatter", etc.
#plt.show()

dados_faturamento = {
    "mes": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
    "faturamento": [30000, 35000, 28000, 40000, 45000, 42000]
}

df_fat = pd.DataFrame(dados_faturamento)
print(df_fat)



# GRAFICO DE LINHA

plt.figure(figsize=(8,4))  # opcional, define o tamanho da figura

df_fat.plot(
    x="mes",
    y="faturamento",
    kind="line",
    marker="o",   # marca os pontos
)

plt.title("Faturamento Mensal")
plt.xlabel("Mês")
plt.ylabel("Faturamento (R$)")
plt.grid(True) # opcional: grade de fundo
plt.tight_layout()  # ajusta o layout para não cortar elementos
plt.show()



# GRAFICO DE BARRAS


plt.figure(figsize=(8, 4))

df_fat.plot(
    x="mes",
    y="faturamento",
    kind="bar"
)

plt.title("Faturamento mensal (barras)")
plt.xlabel("Mês")
plt.ylabel("Faturamento (R$)")
plt.xticks(rotation=0)  # evita rótulos inclinados, se quiser
plt.tight_layout()
plt.show()

print("-------------------------------------------------------------------------------------")


dados_salarios = {
    "salario": [2000, 2200, 2500, 2600, 2800,
                3000, 3200, 3500, 4000, 4500,
                5000, 7000, 8000]
}

df_sal = pd.DataFrame(dados_salarios)
print(df_sal)


plt.figure(figsize=(8, 4))
df_sal["salario"].plot(kind="hist", bins=8)
#número de “caixinhas” (intervalos) do histograma.
#Mais bins → mais detalhes (mas pode ficar ruidoso).
#Menos bins → visão mais geral.

plt.title("Distribuição de salários")
plt.xlabel("Salário (R$)")
plt.ylabel("Frequência")
plt.tight_layout()
plt.show()



#BOX PLOT

#O boxplot resume a distribuição em: quartis, mediana, possíveis outliers.
plt.figure(figsize=(4, 6))

df_sal["salario"].plot(kind="box")

plt.title("Boxplot de salários")
plt.ylabel("Salário (R$)")
plt.tight_layout()
plt.show()
#Linha dentro da caixa → mediana.
#Limites da caixa → Q1 (25%) e Q3 (75%).
#“Bigodes” → valores até 1.5 * IQR.
#Pontos isolados → candidatos a outliers (dependendo do dataset).


print("-------------------------------------------------------------------------------------")

# Gráfico de dispersão (scatter)

dados_imoveis = {
    "preco": [250000, 320000, 500000, 450000, 280000, 600000, 750000, 300000],
    "area_m2": [60, 80, 120, 100, 70, 150, 200, 75]
}

df_imoveis = pd.DataFrame(dados_imoveis)


plt.figure(figsize=(8, 5))

df_imoveis.plot(
    kind="scatter",
    x="area_m2",
    y="preco"
)

plt.title("Dispersão: preço x área do imóvel")
plt.xlabel("Área (m²)")
plt.ylabel("Preço (R$)")
plt.tight_layout()
plt.show()



#Boxplot de várias colunas

plt.figure(figsize=(6, 4))

df_imoveis[["preco", "area_m2"]].plot(kind="box")

plt.title("Boxplot de preço e área")
plt.tight_layout()
plt.show()


print("-------------------------------------------------------------------------------------")

#Salvando gráficos com plt.savefig

plt.figure(figsize=(8, 4))

df_fat.plot(
    x="mes",
    y="faturamento",
    kind="line",
    marker="o"
)

plt.title("Faturamento mensal")
plt.xlabel("Mês")
plt.ylabel("Faturamento (R$)")
plt.grid(True)
plt.tight_layout()

plt.savefig("faturamento_mensal.png", dpi=150)  # salva o arquivo
plt.show()









