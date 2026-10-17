import os
os.environ["LOKY_MAX_CPU_COUNT"] = "4"

import pandas as pd

clientes = {
    "renda_mensal":      [2000, 2500, 3000, 8000, 9000, 10000, 3500, 4000, 7500, 12000],
    "gasto_mensal_loja": [200,  300,  250,  1000, 1100, 1200,  400,  450,  950,  1300]
}

df = pd.DataFrame(clientes)
print(df)


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)  # transforma todas as colunas numéricas

print("Primeiras linhas escaladas:\n", X_scaled[:5])


from sklearn.cluster import KMeans

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10  # número de inicializações diferentes para escolher a melhor
)

df["cluster"] = kmeans.fit_predict(X_scaled)

print(df)
print(df["cluster"].value_counts())


import matplotlib.pyplot as plt

plt.figure(figsize=(6, 5))
plt.scatter(
    df["renda_mensal"],
    df["gasto_mensal_loja"],
    c=df["cluster"],    # cor por cluster
    s=80
)
plt.xlabel("Renda mensal")
plt.ylabel("Gasto mensal na loja")
plt.title("Segmentação de clientes com K-Means (K=3)")
plt.grid(True)
plt.show()


import numpy as np

# Centroides estão no espaço escalado, vamos trazer pro espaço original:
centroides_escalados = kmeans.cluster_centers_
centroides_originais = scaler.inverse_transform(centroides_escalados)

centroides_df = pd.DataFrame(
    centroides_originais,
    columns=["renda_mensal", "gasto_mensal_loja"]
)

print("Centroides (valores médios de cada cluster):\n")
print(centroides_df)



inercia_por_k = []

for k in range(1, 7):  # testar K de 1 a 6
    kmeans_k = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans_k.fit(X_scaled)
    inercia_por_k.append((k, kmeans_k.inertia_))

for k, iner in inercia_por_k:
    print(f"K = {k} -> Inércia: {iner:.2f}")

ks = [item[0] for item in inercia_por_k]
inercias = [item[1] for item in inercia_por_k]

plt.figure(figsize=(6, 4))
plt.plot(ks, inercias, marker="o")
plt.xlabel("Número de clusters (K)")
plt.ylabel("Inércia")
plt.title("Método do cotovelo (elbow) - Exemplo")
plt.grid(True)
plt.show()
