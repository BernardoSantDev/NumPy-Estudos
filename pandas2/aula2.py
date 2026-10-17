import pandas as pd

df = pd.read_csv("vendasp.csv", sep=";", encoding="latin-1")
print(df.head())
print(df.dtypes)


df_pequeno = pd.read_csv(
    "vendasp.csv",
    usecols=["order_id", "valor", "cidade"]
)

print(df_pequeno.head())


df_amostra = pd.read_csv("vendasp.csv", nrows=2)
print(df_amostra)

df_amostra.to_csv("vendas_filtrado.csv", index=False, encoding="utf-8")

#VARIAS ABAS (PAGINAS)
#df_setores = pd.read_excel("rh_empresa.xlsx", sheet_name="nome das abas")
#print(df_setores.head())
