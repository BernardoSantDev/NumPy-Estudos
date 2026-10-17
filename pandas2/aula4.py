import pandas as pd

dados_clientes = {
    "id_cliente": [1, 2, 3, 4, 5],
    "nome": ["Ana", "Bruno", "Carla", "Daniel", "Eduarda"],
    "idade": [22, 35, 29, 42, 31],
    "cidade": ["Juiz de Fora", "São Paulo", "Juiz de Fora", "Rio de Janeiro", "São Paulo"],
    "renda_mensal": [2500.0, 7000.0, 4800.0, 12000.0, 5200.0]
}

df_clientes = pd.DataFrame(dados_clientes)
print(df_clientes)
print(df_clientes["nome"])
print(df_clientes[["nome", "cidade"]])
print(df_clientes.iloc[0])
print(df_clientes.iloc[4])
print(df_clientes.iloc[0:3])
print(df_clientes.iloc[0:2, 1:5])


print(df_clientes.loc[0:2, ["nome", "cidade"]])

print("-------------------------------------------------------------------")

filtro_renda = df_clientes["renda_mensal"] > 5000
print(filtro_renda)

filtro_ricos = df_clientes["renda_mensal"] > 8000
clientes_ricos = df_clientes[filtro_ricos]
print(clientes_ricos)

print("-------------------------------------------------------------------")

filtro = (df_clientes["renda_mensal"] > 5000) & (df_clientes["idade"] > 30)
print(df_clientes[filtro])

cidade = (df_clientes["cidade"] ==  "Juiz de Fora") | (df_clientes["cidade"] == "São Paulo")
print(df_clientes[cidade])

filtro_nao_sp = ~(df_clientes["cidade"] == "São Paulo")
print(df_clientes[filtro_nao_sp])

filtragem = (df_clientes["idade"] > 30) & (df_clientes["renda_mensal"] > 5000)
print(df_clientes.loc[filtragem, ["id_cliente", "cidade"]])
