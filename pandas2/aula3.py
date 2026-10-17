import pandas as pd

dados = {
    "produto": [
        "Camiseta Básica", "Calça Jeans", "Vestido Floral", "Jaqueta Couro",
        "Camiseta Básica", "Calça Jeans", "Shorts Jeans", "Moletom", "Moletom", "Vestido Floral"
    ],
    "categoria": [
        "Camisetas", "Calças", "Vestidos", "Jaquetas",
        "Camisetas", "Calças", "Shorts", "Moletons", "Moletons", "Vestidos"
    ],
    "preco": [49.90, 159.90, 199.90, 399.90, 59.90, 149.90, 89.90, 129.90, 139.90, 219.90],
    "quantidade_vendida": [120, 80, 45, 10, 150, 70, 60, 90, 110, 30]
}

df_loja = pd.DataFrame(dados)
print(df_loja)

print(df_loja.describe())
print(df_loja.describe(include="all"))

print(df_loja["categoria"].unique())
print(df_loja["categoria"].nunique())
print(df_loja["categoria"].value_counts())
print(df_loja["categoria"].value_counts(normalize=True))

print(df_loja["preco"].min())
print(df_loja["preco"].max())
print(df_loja["preco"].mean())


q1 = df_loja["preco"].quantile(0.25)
q2 = df_loja["preco"].quantile(0.50) #mediana
q3 = df_loja["preco"].quantile(0.75)

print(q1, q2, q3)



#outliers

dados = {
    "produto": [
        "Camiseta Básica", "Calça Jeans", "Vestido Floral", "Jaqueta Couro",
        "Camiseta Básica", "Calça Jeans", "Shorts Jeans", "Moletom", "Moletom", "Vestido Floral"
    ],
    "categoria": [
        "Camisetas", "Calças", "Vestidos", "Jaquetas",
        "Camisetas", "Calças", "Shorts", "Moletons", "Moletons", "Vestidos"
    ],
    "preco": [49.90, 159.90, 199.90, 10000, 59.90, 149.90, 89.90, 129.90, 139.90, 219.90],
    "quantidade_vendida": [120, 80, 45, 10, 150, 70, 60, 90, 110, 30]
}
df_loja = pd.DataFrame(dados)

print(df_loja.describe())

#intervalo iterquartilico IQR = Q3 - Q1
#valores menores que Q1-1.5*IQR -> possiveis outliers inferiores
#valores maiores que Q3+1.5*IQR -> possiveis outliers superiores


precos = df_loja["preco"]

q1 = precos.quantile(0.25)
q3 = precos.quantile(0.75)
iqr = q3 - q1

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

print(limite_inferior, limite_superior)
outliers = df_loja[
    (df_loja["preco"] < limite_inferior) |
    (df_loja["preco"] > limite_superior)
]

print(outliers)

print(df_loja.shape)
print(df_loja.dtypes)
print(df_loja.isna().sum())



dados_cursos = {
    "curso": [
        "Python Básico", "Python Avançado", "Data Science com Python",
        "Introdução ao SQL", "Machine Learning", "Excel para Dados",
        "Power BI Essencial", "Estatística Aplicada"
    ],
    "area": [
        "Programação", "Programação", "Data Science",
        "Banco de Dados", "Data Science", "Ferramentas",
        "Ferramentas", "Estatística"
    ],
    "avaliacao": [4.5, 4.7, 4.8, 4.2, 4.6, 4.3, 4.4, 4.1],
    "horas": [12, 20, 25, 10, 30, 8, 15, 18],
    "qtde_alunos": [1200, 800, 950, 600, 700, 1100, 900, 500]
}

df_cursos = pd.DataFrame(dados_cursos)
print(df_cursos)


print(df_cursos["area"].value_counts())
print(df_cursos[["avaliacao", "horas", "qtde_alunos"]].describe())
print(df_cursos.sort_values("qtde_alunos", ascending=False).head(1))
print(df_cursos.sort_values("avaliacao", ascending=False).head(1))










