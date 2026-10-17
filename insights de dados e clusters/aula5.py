import pandas as pd

df = pd.read_csv("insights de dados e clusters/clientes_ecommerce.csv")
print(df.head())
print(df.columns)

features = ["qtd_pedidos", "ticket_medio", "tempo_como_cliente_meses"]
X = df[features]
print(X.head())

print("Valores ausentes por coluna:")
print(X.isna().sum())

#CASO TIVESSE
# 1. Remover linhas com valores ausentes (se forem poucas):
X_clean = X.dropna()
print("Antes:", X.shape)
print("Depois:", X_clean.shape)
df_clean = df.loc[X_clean.index].copy()

from sklearn.preprocessing  import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_clean)
print("Primeiras linhas padronizadas:")
print(X_scaled[:5])

#Treinando com K=3
from sklearn.cluster import KMeans
k=3
kmeans = KMeans(n_clusters=k, random_state=42)
cluster_labels = kmeans.fit_predict(X_scaled)
print("Primeiros 10 rótulos de cluster:")
print(cluster_labels[:10])

df_clean["cluster_kmeans"] = cluster_labels
print(df_clean.head())

cluster_counts = df_clean["cluster_kmeans"].value_counts().sort_index()
print("Contagem de clientes por cluster:")
print(cluster_counts)


import matplotlib.pyplot as plt

plt.scatter(
    df_clean["qtd_pedidos"],
    df_clean["ticket_medio"],
    c=df_clean["cluster_kmeans"]
)
plt.xlabel("Quantidade de pedidos")
plt.ylabel("Ticket médio (R$)")
plt.title("Clientes agrupados por K-Means (K=3)")
plt.show()

#Vamos rodar o mesmo K-Means, mas desta vez usando os dados sem padronizar (X_clean ao invés de X_scaled):
kmeans_no_scale = KMeans(n_clusters=3, random_state=42)
labels_no_scale = kmeans_no_scale.fit_predict(X_clean)

df_clean["cluster_sem_escala"] = labels_no_scale
print(df_clean[["qtd_pedidos", "ticket_medio", "tempo_como_cliente_meses", "cluster_sem_escala"]].head())

plt.scatter(
    df_clean["qtd_pedidos"],
    df_clean["ticket_medio"],
    c=df_clean["cluster_kmeans"]
)
plt.xlabel("Quantidade de pedidos")
plt.ylabel("Ticket médio (R$)")
plt.title("Clusters (com padronização)")
plt.show()

plt.scatter(
    df_clean["qtd_pedidos"],
    df_clean["ticket_medio"],
    c=df_clean["cluster_sem_escala"]
)
plt.xlabel("Quantidade de pedidos")
plt.ylabel("Ticket médio (R$)")
plt.title("Clusters (sem padronização)")
plt.show()

#O que costuma acontecer:
#Sem padronizar, a variável com números maiores (geralmente ticket_medio) domina a distância → os clusters são criados quase que só em função dela.
#Com padronização, qtd_pedidos, ticket_medio e tempo_como_cliente_meses passam a ter peso mais equilibrado.
#Observe se você sente que:
#no caso “sem escala”, os grupos parecem estar mais separados apenas na vertical (ticket),
#enquanto “com escala”, os grupos usam melhor tanto qtd_pedidos quanto ticket_medio.


features = ["qtd_pedidos", "ticket_medio", "tempo_como_cliente_meses"]
resumo_clusters = df_clean.groupby("cluster_kmeans")[features].mean()
print("Resumo dos clusters:")
print(resumo_clusters)

contagem_clusters = df_clean["cluster_kmeans"].value_counts().sort_index()
print("Contagem de clientes por cluster:")
print(contagem_clusters)


def nome_segmento(cluster_id):
    if cluster_id == 0:
        return "Clientes Frequentes"
    elif cluster_id == 1:
        return "Clientes Iniciais"
    elif cluster_id == 2:
        return "Clientes VIP"
    else:
        return "Outro"
    
df_clean["segmento"] = df_clean["cluster_kmeans"].apply(nome_segmento)
print(df_clean[["qtd_pedidos", "ticket_medio", "tempo_como_cliente_meses", "cluster_kmeans", "segmento"]].head())

plt.scatter(
    df_clean["qtd_pedidos"],
    df_clean["ticket_medio"],
    c=df_clean["cluster_kmeans"]
)
plt.xlabel("Quantidade de pedidos")
plt.ylabel("Ticket médio (R$)")
plt.title("Segmentos de clientes (K-Means)")
plt.show()



#ACHANDO A INERCIA

inertias = []
ks = range (2,9) #k de 2 ate 8
for k in ks:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)

plt.plot(ks, inertias, marker="o")
plt.xlabel("Número de clusters (K)")
plt.ylabel("Inércia")
plt.title("Método do cotovelo - clientes e-commerce")
plt.show()

#Silhouette score (coeficiente de silhouette
#Intuição:
#Mede o quão bem cada ponto está dentro do seu cluster e longe dos outros clusters.
#Vai de -1 a 1:
#perto de 1 → ponto muito bem colocado no seu cluster;
#perto de 0 → ponto na “fronteira”, poderia estar em outro cluster;
#negativo → ponto provavelmente está no cluster errado.

from sklearn.metrics import silhouette_score

kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X_scaled)

sil_score = silhouette_score(X_scaled, labels)
print("Silhouette médio para K=3:", sil_score)


from sklearn.metrics import silhouette_score

sil_scores = []
ks = range(2, 9)

for k in ks:
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(X_scaled)
    score = silhouette_score(X_scaled, labels)
    sil_scores.append(score)
    print(f"K={k} -> silhouette={score:.3f}")

plt.plot(ks, sil_scores, marker="o")
plt.xlabel("Número de clusters (K)")
plt.ylabel("Silhouette médio")
plt.title("Silhouette score por K")
plt.show()



