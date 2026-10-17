import pandas as pd

dados_produtos = {
    "produto": [
        "Teclado Mecânico", "Mouse Gamer", "Monitor 24\"", "Headset", "Notebook",
        "Webcam HD", "Cadeira Gamer"
    ],
    "categoria": [
        "Periféricos", "Periféricos", "Monitores", "Periféricos", "Computadores",
        "Periféricos", "Móveis"
    ],
    "custo": [120.0, 60.0, 500.0, 80.0, 2500.0, 70.0, 600.0],
    "preco_venda": [250.0, 150.0, 900.0, 200.0, 4000.0, 160.0, 1300.0],
}
df_prod = pd.DataFrame(dados_produtos)
print(df_prod)

print(df_prod.sort_values("preco_venda"))
print(df_prod.sort_values("preco_venda", ascending=False))


print("-----------------------------------------------------------------------------------")

print(df_prod.sort_values(["categoria", "preco_venda"]))

print(df_prod.sort_values(["categoria", "preco_venda"], ascending=[True, False]))


print("-----------------------------------------------------------------------------------")

df_indexado = df_prod.set_index("produto")
print(df_indexado.sort_index())


print("-----------------------------------------------------------------------------------")

df_prod["lucro"] = df_prod["preco_venda"] - df_prod["custo"]
print(df_prod)
df_prod["margem_pct"] = df_prod["lucro"] / df_prod["preco_venda"] * 100
print(df_prod)


print("-----------------------------------------------------------------------------------")


df_prod2 = (
    df_prod
      .assign(
          lucro = df_prod["preco_venda"] - df_prod["custo"],
          margem_pct = (df_prod["preco_venda"] - df_prod["custo"]) / df_prod["preco_venda"] * 100
      )
)
print(df_prod2)


df_relatorio = (
    df_prod
      .assign(
          lucro = df_prod["preco_venda"] - df_prod["custo"],
          margem_pct = (df_prod["preco_venda"] - df_prod["custo"]) / df_prod["preco_venda"] * 100
      )
      .sort_values("margem_pct", ascending=False)
)
print(df_relatorio)


print("-----------------------------------------------------------------------------------")



df_relatorio["margem_pct"] = df_relatorio["margem_pct"].round(2)
print(df_relatorio)
df_arredondado = df_relatorio.round(2)
print(df_arredondado)



print("-----------------------------------------------------------------------------------")

colunas = ["produto", "custo", "categoria", "lucro", "margem_pct", "preco_venda"]
df_ordenado = df_prod[colunas]
print(df_ordenado)



print("-----------------------------------------------------------------------------------")


import pandas as pd

df_notas = pd.DataFrame({
    "aluno": ["Ana", "Bruno", "Carla", "Daniel"],
    "nota": [9.5, 11.0, -1.0, 7.0]
})

df_notas["nota_corrigida"] = df_notas["nota"].clip(lower=0, upper=10)
print(df_notas)




















