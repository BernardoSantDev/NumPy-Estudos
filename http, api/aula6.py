import pandas as pd

dados = [
    {"id_venda": 1, "produto": "Teclado",     "categoria": "Periféricos", "preco": 200.0, "quantidade": 1, "cidade": "Juiz de Fora"},
    {"id_venda": 2, "produto": "Mouse",       "categoria": "Periféricos", "preco": 150.0, "quantidade": 2, "cidade": "São Paulo"},
    {"id_venda": 3, "produto": "Monitor 24\"", "categoria": "Monitores",  "preco": 900.0, "quantidade": 1, "cidade": "Rio de Janeiro"},
    {"id_venda": 4, "produto": "Cadeira Gamer","categoria": "Móveis",     "preco": 1200.0,"quantidade": 1, "cidade": "Juiz de Fora"},
    {"id_venda": 5, "produto": "Headset",     "categoria": "Periféricos", "preco": 300.0, "quantidade": 1, "cidade": "São Paulo"},
    {"id_venda": 6, "produto": "Mouse",       "categoria": "Periféricos", "preco": 150.0, "quantidade": 3, "cidade": "Rio de Janeiro"}
]

df = pd.DataFrame(dados)

# Criar coluna de valor total da venda
df["valor_total"] = df["preco"] * df["quantidade"]

print(df)


#Primeira exploração: “o que tem aqui?”
print(df.head())   # primeiras linhas
print(df.tail())   # últimas linhas
print(df.shape)    # (n_linhas, n_colunas)
print(df.columns)  # nomes das colunas
print(df.info())   # tipos e quantidade de valores não nulos


#Estatísticas descritivas: describe()
print(df[["preco", "quantidade", "valor_total"]].describe())

print("Preço médio:", df["preco"].mean())
print("Valor total médio:", df["valor_total"].mean())
print("Quantidade máxima:", df["quantidade"].max())
#count – quantidade de valores
#mean – média
#std – desvio padrão
#min, max
#25%, 50%, 75% – quartis

#Distribuição de categorias: value_counts() e unique()
#Valores unicos
print(df["produto"].unique())
print(df["cidade"].unique())

#Contagem de frequencia
print(df["produto"].value_counts())
print(df["cidade"].value_counts())
print(df["categoria"].value_counts())


#Filtrando dados (condições)
#Filtro simples
vendas_sp = df[df["cidade"] == "São Paulo"]
print(vendas_sp)
vendas_alta = df[df["valor_total"] > 300]
print(vendas_alta)

#Combinação de condições
filtro = (df["cidade"] == "Rio de Janeiro") & (df["categoria"] == "Periféricos")
vendas_filtradas = df[filtro]
print(vendas_filtradas)
filtro = (df["cidade"] == "Juiz de Fora") | (df["cidade"] == "São Paulo")
vendas_cidades = df[filtro]
print(vendas_cidades)






#Ordenando dados e pegando “Top N”
#Ordenar com sort_values
df_ordenado = df.sort_values(by="valor_total", ascending=False) #False para ordem decrescente e True para ordem crescente
print(df_ordenado)
df_ordenado = df.sort_values(by=["cidade", "valor_total"], ascending=[True, False])
print(df_ordenado)

#Top N com nlargest
top3 = df.nlargest(3, "valor_total")
print(top3)






#Agrupamento com groupby (resumo por categoria)
#Vendas por cidade
vendas_por_cidade = df.groupby("cidade")["valor_total"].sum()
print(vendas_por_cidade)
vendas_por_cidade = vendas_por_cidade.reset_index()
print(vendas_por_cidade)


#Estatísticas múltiplas por cidade
resumo_cidade = df.groupby("cidade")["valor_total"].agg(["sum", "mean", "max", "count"])
print(resumo_cidade)


#Agrupando por categoria e cidade
resumo_cat_cidade = df.groupby(["categoria", "cidade"])["valor_total"].sum()
print(resumo_cat_cidade)
resumo_cat_cidade = resumo_cat_cidade.reset_index()
print(resumo_cat_cidade)





#Gráficos simples com pandas
import matplotlib.pyplot as plt

vendas_por_cidade = df.groupby("cidade")["valor_total"].sum()

vendas_por_cidade.plot(kind="bar")
plt.title("Valor total de vendas por cidade")
plt.xlabel("Cidade")
plt.ylabel("Valor total")
plt.show()
#Tipos básicos de gráficos:
#kind="bar" – gráfico de barras (ótimo para categorias).
#kind="line" – gráfico de linhas (ótimo para séries temporais).
#kind="hist" – histograma (distribuição de uma variável numérica).
vendas_por_categoria = df.groupby("categoria")["valor_total"].sum()
vendas_por_categoria.plot(kind="bar")
plt.title("Vendas por categoria")
plt.ylabel("Valor total")
plt.show()





#Ligando com Numpy (estatísticas adicionais)
import numpy as np

print("Desvio padrão do valor_total:", np.std(df["valor_total"]))
print("Mediana do valor_total:", np.median(df["valor_total"]))

vendas_rj = df[df["cidade"] == "Rio de Janeiro"]
print("Média das vendas no RJ:", vendas_rj["valor_total"].mean())


