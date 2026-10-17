import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

dados_imoveis = {
    "preco": [250000, 320000, 500000, 450000, 280000, 600000, 750000, 300000, 520000, 680000],
    "area_m2": [60, 80, 120, 100, 70, 150, 200, 75, 130, 160],
    "quartos": [2, 3, 3, 3, 2, 4, 4, 2, 3, 4],
    "banheiros": [1, 2, 2, 3, 1, 3, 3, 2, 2, 3]
}

df_imoveis = pd.DataFrame(dados_imoveis)
print(df_imoveis)

#sns.pairplot(df_imoveis)
#plt.show()

#sns.pairplot(df_imoveis[["preco", "area_m2", "quartos"]])
#plt.show()

#sns.pairplot(df_imoveis, diag_kind="kde")
#plt.show()

#diag_kind="hist" (padrão) → histogramas.
#diag_kind="kde" → curvas de densidade.

df_imoveis["tipo"] = ["Apartamento", "Apartamento", "Casa", "Casa", "Apartamento",
                      "Casa", "Casa", "Apartamento", "Casa", "Casa"]
print(df_imoveis)

#sns.pairplot(df_imoveis, vars=["preco", "area_m2", "quartos"],
#             hue="tipo", diag_kind="kde")
#plt.show()


dados_saude = {
    "idade": [18, 20, 22, 25, 28, 30, 35, 40, 45, 50, 55, 60],
    "peso": [60, 62, 65, 68, 70, 75, 78, 80, 82, 78, 75, 72],
    "altura": [1.65, 1.70, 1.72, 1.75, 1.70, 1.80, 1.78, 1.76, 1.74, 1.72, 1.70, 1.68]
}

df_saude = pd.DataFrame(dados_saude)
print(df_saude)


#sns.jointplot(
#    data=df_saude,
#    x="idade",
#    y="peso",
#    kind="scatter"
#)
#plt.show()


sns.jointplot(
    data=df_saude,
    x="idade",
    y="peso",
    kind="reg"
)
plt.show()


sns.jointplot(
    data=df_saude,
    x="idade",
    y="peso",
    kind="kde",
    fill=True
)
plt.show()
#Regiões mais escuras indicam maior concentração de pontos.
#É útil para enxergar “nuvens” de maior densidade, especialmente em datasets maiores.

print(df_imoveis.corr(numeric_only=True))
sns.pairplot(df_imoveis[["preco", "area_m2", "quartos", "banheiros"]])
plt.show()
sns.jointplot(data=df_imoveis, x="area_m2", y="preco", kind="reg")
plt.show()


#Algumas orientações práticas:
#Pairplot funciona melhor com:
#3 a 6 variáveis numéricas.
#Se usar em 15 colunas, o gráfico fica confuso e pesado.
#Jointplot é ótimo para:
#Casos em que você tem um par de variáveis especialmente importante.
#Comunicar uma relação que você quer destacar.
#Use hue com cuidado:
#Poucas categorias (ex.: 2 ou 3) funcionam bem.
#Muitas categorias tornam o gráfico confuso.
#Sempre combine visualização com números:
#Correlação (df.corr) ajuda a quantificar o que você vê.
#Estatísticas descritivas (describe) ajudam a interpretar escalas e outliers.
#Lembre que esses gráficos são exploratórios:
#Eles não “provam” causalidade.
#Servem para gerar hipóteses e insights.


