import pandas as pd

dados = {
    "dia": list(range(1, 16)),
    "faturamento": [3000, 3200, 3100, 2900, 3050,
                    2950, 3100, 3000, 3050, 3100,
                    2900, 2950, 3000, 2900, 50000]  # último dia com valor muito alto
}

df_fat = pd.DataFrame(dados)
print(df_fat)

print(df_fat["faturamento"].describe())


f = df_fat["faturamento"]

q1 = f.quantile(0.25)
q3 = f.quantile(0.75)
iqr = q3 - q1

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

print(limite_inferior, limite_superior)

outliers = df_fat[
    (df_fat["faturamento"] < limite_inferior) |
    (df_fat["faturamento"] > limite_superior)
]
print(outliers)

print("-------------------------------------")

#Removendo outliers
df_sem_outliers = df_fat[
    (df_fat["faturamento"] >= limite_inferior) &
    (df_fat["faturamento"] <= limite_superior)
]
print(df_sem_outliers)

print("-------------------------------------")

df_clipado = df_fat.copy()
df_clipado["faturamento_limpo"] = df_clipado["faturamento"].clip(upper=limite_superior)
print(df_clipado)
print(df_fat["faturamento"].mean(), df_clipado["faturamento_limpo"].mean())

print("------------------------------------------------------------------------------------------------------------------------")



dados_pag = {
    "id_venda": [1, 2, 3, 4, 5, 6],
    "forma_pagamento": ["Crédito", "Débito", "Crédito", "Pix", "Dinheiro", "Crédito"],
    "valor": [100, 50, 200, 80, 40, 150]
}

df_pag = pd.DataFrame(dados_pag)
print(df_pag)

df_pag["forma_pagamento"] = df_pag["forma_pagamento"].astype("category")
print(df_pag.dtypes)

print(df_pag["forma_pagamento"].cat.categories)
print(df_pag["forma_pagamento"].cat.codes)

df_pag["forma_pagamento"] = df_pag["forma_pagamento"].str.lower()
print(df_pag["forma_pagamento"])

df_pag["forma_pagamento"] = df_pag["forma_pagamento"].astype("category")
print(df_pag["forma_pagamento"].cat.categories)


print("------------------------------------------------------------------------------------------------------------------------")

import pandas as pd

datas = pd.date_range(start="2024-10-01", periods=10, freq="D")

dados = {
    "data": datas,
    "loja": ["Centro", "Centro", "Shopping", "Shopping", "Centro",
             "Centro", "Shopping", "Centro", "Shopping", "Centro"],
    "faturamento": [3000, 3200, 5000, 4500, 2800, 2900, 5200, 3100, 4800, 3500]
}

df_vendas = pd.DataFrame(dados)
print(df_vendas)

df_vendas["ano"] = df_vendas["data"].dt.year
df_vendas["mes"] = df_vendas["data"].dt.month
df_vendas["dia"] = df_vendas["data"].dt.day
print(df_vendas)

df_vendas["dia_da_semana_num"] = df_vendas["data"].dt.weekday  # 0=segunda, 6=domingo
df_vendas["dia_da_semana_nome"] = df_vendas["data"].dt.day_name(locale="pt_BR.utf8")
print(df_vendas)
























