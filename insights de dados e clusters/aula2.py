import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("insights de dados e clusters/clientes_ecommerce.csv")
print(df.head())
print(df.columns)
print(df.describe())
print(df.describe().T)
print(df.info())

df["ticket_medio"].hist(bins=20)
plt.xlabel("Ticket médio (R$)")
plt.ylabel("Quantidade de clientes")
plt.title("Distribuição do ticket médio")
plt.show()

plt.scatter(df["qtd_pedidos"], df["ticket_medio"])
plt.xlabel("Quantidade de pedidos")
plt.ylabel("Ticket médio (R$)")
plt.title("Clientes: pedidos x ticket médio")
plt.show()









