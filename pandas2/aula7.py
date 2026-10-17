import pandas as pd
import numpy as np

dados_clientes = {
    "id_cliente": [1, 2, 3, 4, 4],
    "nome": ["Ana", "Bruno", "Carla", "Daniel", "Daniel"],
    "idade": [25, np.nan, 32, 40, 40],
    "renda": [3000.0, 7000.0, np.nan, 12000.0, 12000.0],
    "cidade": ["Juiz de Fora", "São Paulo", None, "Rio de Janeiro", "Rio de Janeiro"]
}

df_clientes = pd.DataFrame(dados_clientes)
print(df_clientes)

print(df_clientes.isna())
print(df_clientes.isna().sum())
print(df_clientes.notna().sum())

df_sem_nulos = df_clientes.dropna()
print(df_sem_nulos)


#você só quer remover linhas se renda for nulo, mas não se cidade estiver em branco.
df_sem_renda_nula = df_clientes.dropna(subset=["renda"])
print(df_sem_renda_nula)

#Em vez de remover linhas, muitas vezes é melhor preencher valores nulos com algo razoável.
#Isso depende do contexto:
#Preencher idade com a média ou mediana.
#Preencher cidade com "Desconhecida".
#Preencher renda com 0 em casos específicos (por exemplo, se 0 fizer sentido).

print("------------------------------------------------------------------------------------------------------------------")

#VALOR FIXO
df_clientes["cidade"].fillna("Desconhecida", inplace=True)
print(df_clientes)

#MEDIA DA COLUNA
media_renda = df_clientes["renda"].mean()
df_clientes["renda"].fillna(media_renda, inplace=True)
print(df_clientes)

#mediana da coluna
mediana_idade = df_clientes["idade"].median()
df_clientes["idade"].fillna(mediana_idade, inplace=True)
print(df_clientes)

print(df_clientes.isna().sum())


print("------------------------------------------------------------------------------------------------------------------")


#DUPLICATAS

print(df_clientes.duplicated())

print(df_clientes[df_clientes.duplicated()])

print(df_clientes.duplicated(subset=["id_cliente"]))

df_sem_duplicatas = df_clientes.drop_duplicates()
print(df_sem_duplicatas)

df_sem_duplicatas_id = df_clientes.drop_duplicates(subset=["id_cliente"])
print(df_sem_duplicatas_id)


print("------------------------------------------------------------------------------------------------------------------")


dados_pedidos = {
    "id_pedido": ["1", "2", "3", "4"],
    "data_pedido": ["2024-10-01", "2024-10-02", "2024/10/03", "2024-10-04"],
    "valor": ["200.50", "350,00", "150.00", "abc"]
}

df_pedidos = pd.DataFrame(dados_pedidos)
print(df_pedidos)
print(df_pedidos.dtypes)


#Convertendo datas com to_datetime
#errors="raise" (padrão): lança erro se algo estiver errado.
#errors="coerce": valores inválidos viram NaT (equivalente a nulo para datas).
#errors="ignore": deixa como está se der problema.

df_pedidos["data_pedido"] = pd.to_datetime(df_pedidos["data_pedido"], errors="coerce")
print(df_pedidos)
print(df_pedidos.dtypes)


#Convertendo números com to_numeric

df_pedidos["valor_limpo"] = df_pedidos["valor"].str.replace(",", ".", regex = False)
df_pedidos["valor_num"] = pd.to_numeric(df_pedidos["valor_limpo"], errors = "coerce")
print(df_pedidos)
print(df_pedidos.dtypes)

df_pedidos["valor_num"].fillna(0, inplace=True)
print(df_pedidos)

#Convertendo tipos simples com astype

df_pedidos["id_pedido"] = df_pedidos["id_pedido"].astype("int64")
print(df_pedidos)
print(df_pedidos.dtypes)



