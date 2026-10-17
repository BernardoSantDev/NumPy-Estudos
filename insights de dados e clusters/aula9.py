import pandas as pd
import os
import matplotlib.pyplot as plt
os.environ["LOKY_MAX_CPU_COUNT"] = "4"

df_tx = pd.read_csv("../transacoes_simples.csv")
print(df_tx.head())
print(df_tx.info())
print(df_tx[["valor_transacao", "qtd_transacoes_dia"]].describe().T)

features = ["valor_transacao", "qtd_transacoes_dia"]
X = df_tx[features]
print(X.isna().sum())
X = X.dropna()
df_tx_clean = df_tx.loc[X.index].copy()

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Primeiras linhas padronizadas:")
print(X_scaled[:5])

from sklearn.cluster import DBSCAN

dbscan = DBSCAN(eps=0.5, min_samples=2)
labels = dbscan.fit_predict(X_scaled)

print("Rótulos encontrados:", set(labels))
df_tx_clean["cluster_dbscan"] = labels
print(df_tx_clean.head())

import numpy as np

num_ruidos = np.sum(df_tx_clean["cluster_dbscan"] == -1)
total = len(df_tx_clean)
print(f"Transações marcadas como ruído: {num_ruidos} de {total} ({num_ruidos/total:.2%})")

df_suspeitas = df_tx_clean[df_tx_clean["cluster_dbscan"] == -1]
print("Algumas transações suspeitas:")
print(df_suspeitas.head())

import matplotlib.pyplot as plt

plt.scatter(
    df_tx_clean["valor_transacao"],
    df_tx_clean["qtd_transacoes_dia"],
    c=df_tx_clean["cluster_dbscan"]
)
plt.xlabel("Valor da transação (R$)")
plt.ylabel("Quantidade de transações no dia")
plt.title("DBSCAN em transações financeiras simples")
plt.show()





for eps in [0.4, 0.7, 1.0, 1.3]:
    db = DBSCAN(eps=eps, min_samples=5)
    labels_test = db.fit_predict(X_scaled)
    num_ruidos = np.sum(labels_test == -1)
    print(f"eps={eps} -> clusters: {set(labels_test)}, ruídos: {num_ruidos}")

eps_escolhido = 0.7

for m in [3, 5, 10]:
    db = DBSCAN(eps=eps_escolhido, min_samples=m)
    labels_test = db.fit_predict(X_scaled)
    num_ruidos = np.sum(labels_test == -1)
    print(f"min_samples={m} -> clusters: {set(labels_test)}, ruídos: {num_ruidos}")


eps_values = [0.3, 0.5, 0.7, 1.0, 1.3]
resultados_eps = []

for eps in eps_values:
    db = DBSCAN(eps=eps, min_samples=5)
    labels = db.fit_predict(X_scaled)
    clusters_unicos = set(labels)
    num_ruidos = np.sum(labels == -1)
    num_clusters = len(clusters_unicos) - (1 if -1 in clusters_unicos else 0)

    resultados_eps.append({
        "eps": eps,
        "num_clusters": num_clusters,
        "num_ruidos": num_ruidos
    })

for r in resultados_eps:
    print(f"eps={r['eps']} -> clusters={r['num_clusters']}, ruídos={r['num_ruidos']}")




import pandas as pd

from sklearn.preprocessing import StandardScaler

df_tx = pd.read_csv("../transacoes_simples.csv")
features = ["valor_transacao", "qtd_transacoes_dia"]

X = df_tx[features].dropna()

df_tx_clean = df_tx.loc[X.index].copy()

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)


import numpy as np
from sklearn.cluster import DBSCAN

eps_values = [0.3, 0.5, 0.7, 1.0, 1.3]
resultados_eps = []

for eps in eps_values:
    db = DBSCAN(eps=eps, min_samples=5)
    labels = db.fit_predict(X_scaled)
    clusters_unicos = set(labels)
    num_ruidos = np.sum(labels == -1)
    num_clusters = len(clusters_unicos) - (1 if -1 in clusters_unicos else 0)

    resultados_eps.append({
        "eps": eps,
        "num_clusters": num_clusters,
        "num_ruidos": num_ruidos
    })

for r in resultados_eps:
    print(f"eps={r['eps']} -> clusters={r['num_clusters']}, ruídos={r['num_ruidos']}")



eps_escolhido = 0.7
min_samples_values = [3, 5, 8, 12]
resultados_min_samples = []

for m in min_samples_values:
    db = DBSCAN(eps=eps_escolhido, min_samples=m)
    labels = db.fit_predict(X_scaled)
    clusters_unicos = set(labels)
    num_ruidos = np.sum(labels == -1)
    num_clusters = len(clusters_unicos) - (1 if -1 in clusters_unicos else 0)

    resultados_min_samples.append({
        "min_samples": m,
        "num_clusters": num_clusters,
        "num_ruidos": num_ruidos
    })

for r in resultados_min_samples:
    print(f"min_samples={r['min_samples']} -> clusters={r['num_clusters']}, ruídos={r['num_ruidos']}")


eps_final = 0.7      # troque pelo que escolheu
min_samples_final = 5

db_final = DBSCAN(eps=eps_final, min_samples=min_samples_final)
labels_final = db_final.fit_predict(X_scaled)

df_tx_clean["cluster_dbscan"] = labels_final


import matplotlib.pyplot as plt

plt.scatter(
    df_tx_clean["valor_transacao"],
    df_tx_clean["qtd_transacoes_dia"],
    c=df_tx_clean["cluster_dbscan"]
)
plt.xlabel("Valor da transação (R$)")
plt.ylabel("Qtd transações no dia")
plt.title(f"DBSCAN (eps={eps_final}, min_samples={min_samples_final})")
plt.show()

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, random_state=42)
labels_kmeans = kmeans.fit_predict(X_scaled)

df_tx_clean["cluster_kmeans"] = labels_kmeans

plt.scatter(
    df_tx_clean["valor_transacao"],
    df_tx_clean["qtd_transacoes_dia"],
    c=df_tx_clean["cluster_kmeans"]
)
plt.xlabel("Valor da transação (R$)")
plt.ylabel("Qtd transações no dia")
plt.title("K-Means (K=3) em transações")
plt.show()

print("DBSCAN - contagem por cluster:")
print(df_tx_clean["cluster_dbscan"].value_counts().sort_index())
print("K-Means - contagem por cluster:")
print(df_tx_clean["cluster_kmeans"].value_counts().sort_index())

print("DBSCAN - resumo dos clusters (sem ruído):")
print(df_tx_clean[df_tx_clean["cluster_dbscan"] != -1]
      .groupby("cluster_dbscan")[features].mean())

print("K-Means - resumo dos clusters:")
print(df_tx_clean.groupby("cluster_kmeans")[features].mean())


