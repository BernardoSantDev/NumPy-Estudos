# ============================================================
# AULA 11 - CLUSTERIZAÇÃO DE CLIENTES DE CARTÃO DE CRÉDITO
# ============================================================


# ============================================================
# 1. IMPORTAÇÃO E LEITURA DOS DADOS
# ============================================================

import pandas as pd

df_cc = pd.read_csv("cartao_credito_clientes.csv")

print(df_cc.head())

print(df_cc.info())


# ============================================================
# 2. ESTATÍSTICAS DESCRITIVAS
# ============================================================

colunas_numericas = [
    "idade",
    "renda_mensal",
    "limite_credito",
    "saldo_atual",
    "gasto_medio_3m",
    "pagamento_medio_3m",
    "percentual_utilizacao_limite",
    "atrasos_ultimos_6m"
]

print(df_cc[colunas_numericas].describe().T)


# ============================================================
# 3. ANÁLISE VISUAL DOS DADOS
# ============================================================

import matplotlib.pyplot as plt


# Distribuição da idade
df_cc["idade"].hist(bins=20)

plt.xlabel("Idade")
plt.ylabel("Quantidade de clientes")
plt.title("Distribuição de idade dos clientes de cartão")

plt.show()


# Distribuição do limite de crédito
df_cc["limite_credito"].hist(bins=30)

plt.xlabel("Limite de crédito (R$)")
plt.ylabel("Quantidade de clientes")
plt.title("Distribuição do limite de crédito")

plt.show()


# Distribuição da utilização do limite
df_cc["percentual_utilizacao_limite"].hist(bins=30)

plt.xlabel("Uso do limite (%)")
plt.ylabel("Quantidade de clientes")
plt.title("Distribuição do uso do limite")

plt.show()


# Limite x saldo
plt.scatter(
    df_cc["limite_credito"],
    df_cc["saldo_atual"],
    alpha=0.5
)

plt.xlabel("Limite de crédito (R$)")
plt.ylabel("Saldo atual (R$)")
plt.title("Limite x Saldo atual")

plt.show()


# Renda x limite
plt.scatter(
    df_cc["renda_mensal"],
    df_cc["limite_credito"],
    alpha=0.5
)

plt.xlabel("Renda mensal (R$)")
plt.ylabel("Limite de crédito (R$)")
plt.title("Renda mensal x Limite de crédito")

plt.show()


# Uso do limite x atrasos
plt.scatter(
    df_cc["percentual_utilizacao_limite"],
    df_cc["atrasos_ultimos_6m"],
    alpha=0.5
)

plt.xlabel("Uso do limite (%)")
plt.ylabel("Atrasos nos últimos 6 meses")
plt.title("Uso do limite x Atrasos")

plt.show()


# ============================================================
# 4. SELEÇÃO DAS FEATURES PARA CLUSTERIZAÇÃO
# ============================================================

features_cluster = [
    "renda_mensal",
    "limite_credito",
    "percentual_utilizacao_limite",
    "atrasos_ultimos_6m"
]

X_cc = df_cc[features_cluster]

print(X_cc.head())


# ============================================================
# 5. VERIFICAR VALORES AUSENTES
# ============================================================

print("Valores ausentes por coluna:")

print(X_cc.isna().sum())


# Remover linhas com valores ausentes
X_cc = X_cc.dropna()

# Manter somente os clientes utilizados na análise
df_cc_clean = df_cc.loc[X_cc.index].copy()

print("Formato após dropna:", X_cc.shape)


# ============================================================
# 6. PADRONIZAÇÃO DOS DADOS
# ============================================================

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X_cc)

print("Primeiras linhas padronizadas:")

print(X_scaled[:5])


# ============================================================
# 7. K-MEANS - MÉTODO DO COTOVELO
# ============================================================

from sklearn.cluster import KMeans

inertias = []

ks = range(2, 9)  # K de 2 até 8

for k in ks:

    kmeans = KMeans(
        n_clusters=k,
        random_state=42
    )

    kmeans.fit(X_scaled)

    inertias.append(kmeans.inertia_)


# Gráfico do cotovelo

plt.plot(
    ks,
    inertias,
    marker="o"
)

plt.xlabel("Número de clusters (K)")
plt.ylabel("Inércia")
plt.title("Método do cotovelo - clientes de cartão de crédito")

plt.show()


# ============================================================
# 8. SILHOUETTE SCORE
# ============================================================

from sklearn.metrics import silhouette_score

sil_scores = []

for k in ks:

    kmeans = KMeans(
        n_clusters=k,
        random_state=42
    )

    labels = kmeans.fit_predict(X_scaled)

    score = silhouette_score(
        X_scaled,
        labels
    )

    sil_scores.append(score)

    print(
        f"K={k} -> silhouette={score:.3f}"
    )


# Gráfico do silhouette

plt.plot(
    ks,
    sil_scores,
    marker="o"
)

plt.xlabel("Número de clusters (K)")
plt.ylabel("Silhouette médio")
plt.title("Silhouette score - clientes de cartão")

plt.show()


# ============================================================
# 9. K-MEANS FINAL
# ============================================================

# K escolhido para a análise
k_escolhido = 4

kmeans_final = KMeans(
    n_clusters=k_escolhido,
    random_state=42
)

labels_final = kmeans_final.fit_predict(X_scaled)

# Adicionar cluster ao DataFrame
df_cc_clean["cluster_kmeans"] = labels_final


# Quantidade de clientes por cluster

print("Quantidade de clientes por cluster - K-Means:")

print(
    df_cc_clean["cluster_kmeans"]
    .value_counts()
    .sort_index()
)


# ============================================================
# 10. RESUMO DOS CLUSTERS - K-MEANS
# ============================================================

resumo_clusters = (
    df_cc_clean
    .groupby("cluster_kmeans")[features_cluster]
    .mean()
)

print("\nResumo dos clusters - K-Means:")

print(resumo_clusters)


# ============================================================
# 11. GRÁFICO K-MEANS - LIMITE X UTILIZAÇÃO
# ============================================================

plt.scatter(
    df_cc_clean["limite_credito"],
    df_cc_clean["percentual_utilizacao_limite"],
    c=df_cc_clean["cluster_kmeans"],
    alpha=0.7
)

plt.xlabel("Limite de crédito (R$)")
plt.ylabel("Uso do limite (%)")

plt.title(
    f"Clientes de cartão – K-Means (K={k_escolhido})"
)

plt.show()


# ============================================================
# 12. GRÁFICO K-MEANS - RENDA X LIMITE
# ============================================================

plt.scatter(
    df_cc_clean["renda_mensal"],
    df_cc_clean["limite_credito"],
    c=df_cc_clean["cluster_kmeans"],
    alpha=0.7
)

plt.xlabel("Renda mensal (R$)")
plt.ylabel("Limite de crédito (R$)")

plt.title(
    f"Renda x Limite – K-Means (K={k_escolhido})"
)

plt.show()


# ============================================================
# 13. HAC - HIERARCHICAL AGGLOMERATIVE CLUSTERING
# ============================================================

import numpy as np


# ------------------------------------------------------------
# Amostra de 50 clientes para o dendrograma
# ------------------------------------------------------------

amostra_indices = np.random.choice(
    X_scaled.shape[0],
    size=50,
    replace=False
)

X_sample = X_scaled[amostra_indices]


# ============================================================
# 14. DENDROGRAMA
# ============================================================

from scipy.cluster.hierarchy import dendrogram, linkage

Z = linkage(
    X_sample,
    method="ward"
)


plt.figure(figsize=(12, 5))

dendrogram(Z)

plt.title(
    "Dendrograma - Amostra de clientes de cartão"
)

plt.xlabel("Clientes (amostra)")
plt.ylabel("Distância (Ward)")

plt.show()


# ============================================================
# 15. HAC FINAL
# ============================================================

from sklearn.cluster import AgglomerativeClustering

n_clusters = 4

hac = AgglomerativeClustering(
    n_clusters=n_clusters,
    linkage="ward"
)

labels_hac = hac.fit_predict(X_scaled)


# Adicionar resultado HAC ao MESMO DataFrame
df_cc_clean["cluster_hac"] = labels_hac


# ============================================================
# 16. QUANTIDADE DE CLIENTES POR CLUSTER - HAC
# ============================================================

print("\nQuantidade de clientes por cluster - HAC:")

print(
    df_cc_clean["cluster_hac"]
    .value_counts()
    .sort_index()
)


# ============================================================
# 17. RESUMO DOS CLUSTERS - HAC
# ============================================================

resumo_hac = (
    df_cc_clean
    .groupby("cluster_hac")[features_cluster]
    .mean()
)

print("\nResumo dos clusters - HAC:")

print(resumo_hac)


# ============================================================
# 18. GRÁFICO HAC - LIMITE X UTILIZAÇÃO
# ============================================================

plt.scatter(
    df_cc_clean["limite_credito"],
    df_cc_clean["percentual_utilizacao_limite"],
    c=df_cc_clean["cluster_hac"],
    alpha=0.7
)

plt.xlabel("Limite de crédito (R$)")
plt.ylabel("Uso do limite (%)")

plt.title(
    f"HAC (Ward) - Limite x Uso do limite (K={n_clusters})"
)

plt.show()


# ============================================================
# 19. GRÁFICO HAC - RENDA X LIMITE
# ============================================================

plt.scatter(
    df_cc_clean["renda_mensal"],
    df_cc_clean["limite_credito"],
    c=df_cc_clean["cluster_hac"],
    alpha=0.7
)

plt.xlabel("Renda mensal (R$)")
plt.ylabel("Limite de crédito (R$)")

plt.title(
    f"HAC (Ward) - Renda x Limite (K={n_clusters})"
)

plt.show()


# ============================================================
# 20. COMPARAÇÃO K-MEANS X HAC
# ============================================================

print("\n===================================")
print("COMPARAÇÃO K-MEANS X HAC")
print("===================================")


print("\nK-Means:")

print(
    df_cc_clean["cluster_kmeans"]
    .value_counts()
    .sort_index()
)


print("\nHAC:")

print(
    df_cc_clean["cluster_hac"]
    .value_counts()
    .sort_index()
)


# ============================================================
# 21. TABELA DE COMPARAÇÃO
# ============================================================

comparacao = pd.crosstab(
    df_cc_clean["cluster_kmeans"],
    df_cc_clean["cluster_hac"]
)

print("\nComparação entre os clusters:")

print(comparacao)