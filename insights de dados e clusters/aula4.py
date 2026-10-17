import numpy as np
import matplotlib.pyplot as plt

# Cada linha: [qtd_compras, ticket_medio]
X = np.array([
    [1, 50], [2, 45], [1, 60],       # grupo 1: poucos pedidos, ticket baixo
    [10, 200], [12, 220], [9, 180],  # grupo 2: muitos pedidos, ticket médio
    [4, 500], [5, 550], [6, 600]     # grupo 3: poucos pedidos, ticket alto
])

plt.scatter(X[:, 0], X[:, 1])
plt.xlabel("Quantidade de compras")
plt.ylabel("Ticket médio (R$)")
plt.title("Clientes (antes do clustering)")
plt.show()

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X)

print("Rótulos dos clusters:", labels)
print("Centróides:")
print(kmeans.cluster_centers_)


# Visualizando os clusters
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    marker="X",
    s=200
)
plt.xlabel("Quantidade de compras")
plt.ylabel("Ticket médio (R$)")
plt.title("Clientes agrupados por K-Means")
plt.show()







import pandas as pd
from sklearn.preprocessing import StandardScaler

# 1. Ler o CSV
df = pd.read_csv("insights de dados e clusters/clientes_ecommerce.csv")

# 2. Escolher features
features = ["qtd_pedidos", "ticket_medio", "tempo_como_cliente_meses"]
X = df[features]

# 3. Remover valores ausentes
X = X.dropna()

# (Opcional: manter um df sincronizado com X)
df_clean = df.loc[X.index].copy()

# 4. Padronizar
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 5. Aplicar K-Means - Treinar o modelo
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
cluster_labels = kmeans.fit_predict(X_scaled)
print(cluster_labels[:10])

# 6. Colocar o cluster no DataFrame
df_clean["cluster_kmeans"] = cluster_labels
print(df_clean.head())

# 7. Visualizar os clusters
import matplotlib.pyplot as plt
plt.scatter(
    df_clean["qtd_pedidos"],
    df_clean["ticket_medio"],
    c=df_clean["cluster_kmeans"]
)
plt.xlabel("Quantidade de pedidos")
plt.ylabel("Ticket médio (R$)")
plt.title("Clientes agrupados por K-Means (3 clusters)")
plt.show()






