import pandas as pd

dados_vendas = {
    "id_venda": [1, 2, 3, 4, 5, 6, 7, 8],
    "cidade": [
        "Juiz de Fora", "Juiz de Fora", "São Paulo", "São Paulo",
        "Rio de Janeiro", "Rio de Janeiro", "Juiz de Fora", "São Paulo"
    ],
    "canal_venda": [
        "Online", "Loja Física", "Online", "Marketplace",
        "Loja Física", "Online", "Online", "Loja Física"
    ],
    "valor": [200.0, 350.0, 500.0, 300.0, 800.0, 150.0, 400.0, 250.0]
}

df_vendas = pd.DataFrame(dados_vendas)
print(df_vendas)

print("-----------------------------------------------------------------------------------")


faturamento_por_cidade = df_vendas.groupby("cidade")["valor"].sum()
print(faturamento_por_cidade)

faturamento_por_cidade = df_vendas.groupby("cidade", as_index=False)["valor"].sum()
print(faturamento_por_cidade)


print("-----------------------------------------------------------------------------------")


print(df_vendas.groupby("cidade")["valor"].mean())   # média por cidade
print(df_vendas.groupby("cidade")["valor"].count())  # quantidade de vendas
print(df_vendas.groupby("cidade")["valor"].max())    # maior venda em cada cidade


print("-----------------------------------------------------------------------------------")


agrupado = df_vendas.groupby(["cidade", "canal_venda"])["valor"].sum()
print(agrupado)


print("-----------------------------------------------------------------------------------")

#O agg permite calcular várias estatísticas de uma vez.

resumo_cidade = df_vendas.groupby("cidade")["valor"].agg(["sum", "mean", "count"])
print(resumo_cidade)


resumo_cidade = df_vendas.groupby("cidade")["valor"].agg(
    total_faturado="sum",
    ticket_medio="mean",
    qtde_vendas="count"
)
print(resumo_cidade)

resumo_cidade = resumo_cidade.reset_index()
print(resumo_cidade)



print("-----------------------------------------------------------------------------------")

#pivot_table é uma forma mais “direta” de criar tabelas estilo Excel (tabela dinâmica).
#values → qual coluna será agregada (ex.: valor)
#index → o que será linha (ex.: cidade)
#columns → o que será coluna (ex.: canal_venda)
#aggfunc → qual função usar ("sum", "mean", "count", etc.)
#fill_value → o que colocar quando não houver valor (ex.: 0)

tabela = pd.pivot_table(
    df_vendas,
    values="valor",
    index="cidade",
    columns="canal_venda",
    aggfunc="sum",
    fill_value=0
)

print(tabela)





