#revisando

import pandas as pd

dados = {
    "id_venda": [1,2,3],
    "loja": ["Centro", "Shopping", "Centro"],
    "produto": ["Teclado", "Mouse", "Monitor"],
    "valor": [200.0, 150.0, 900.0],
}

df_vendas = pd.DataFrame(dados)
print(df_vendas)



df_csv = pd.read_csv("teste.csv")
print(df_csv)


df_renomeado = df_csv.rename(columns={"valor": "valor_venda"})
print(df_renomeado)


df_renomeado = df_csv.rename(columns={
    "valor": "valor_vendas",
    "loja": "nome_loja",    
    "produto": "nome_produto"
})
print(df_renomeado)

df_vendas = pd.read_csv("teste.csv")
print(df_vendas.dtypes)
df_vendas["loja"] = df_vendas["loja"].astype("category")
print(df_vendas)
print(df_vendas.dtypes)


dados = {
    "id_venda": [1, 2, 3],
    "data": ["2024-10-01", "2024-10-02", "2024-10-03"],
    "valor": [200.0, 150.0, 900.0]
}
df_datas = pd.DataFrame(dados)
print(df_datas)
print(df_datas.dtypes)
df_datas["data"] = pd.to_datetime(df_datas["data"])
print(df_datas.dtypes)


df_vendas = pd.DataFrame(dados)
df_vendas.loc[df_vendas["valor"] > 300, "valor_com_desconto"] = df_vendas["valor"] * 0.9
print(df_vendas)


df_vendas = pd.DataFrame(dados)
df_caros = df_vendas[df_vendas["valor"] > 300].copy()
df_caros["valor_com_desconto"] = df_caros["valor"] * 0.9
print(df_caros)

