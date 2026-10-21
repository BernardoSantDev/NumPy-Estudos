#Dataset: cartao_credito_clientes.csv
#Foco: criar perfis de risco/uso do cartão combinando:
#renda,
#limite,
#percentual de uso,
#atrasos.
#Algoritmos principais:
#K-Means (segmentação)
#HAC (comparar estrutura de grupos)
#DBSCAN (opcional, para achar clientes muito fora da curva)

#Ver meus dados e analisar oq importante para o modelo, quais features usar, etc.
import pandas as pd

df = pd.read_csv('insights de dados e clusters/cartao_credito_clientes.csv')
print(df.head())
print(df.info())
print(df.describe().T)

#Escolher features para o modelo de 3 a 6
features = [
    'renda_mensal',
    'limite_credito',
    'percentual_utilizacao_limite',
    'atrasos_ultimos_6m'
]
X = df[features].dropna() #esse comando remove os valores nulos do df, mas perde a referência do index original, então é preciso criar um novo df com os dados limpos, sem valores nulos, para não perder a referência do index original
df_clean = df.loc[X.index].copy() #esse comando cria um novo df com os dados limpos, sem valores nulos, para não perder a referência do index original (x.index é o index do df original, que foi limpo pelo dropna())
print(df_clean.info())

#Padronizando dados para o modelo
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


#K-Means + Método do Cotovelo + Silhueta
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

inertias = []
ks = range(2, 9)

for k in ks:
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X_scaled)
    inertias.append(km.inertia_)

plt.plot(ks, inertias, marker="o")
plt.xlabel("K")
plt.ylabel("Inércia")
plt.title("Método do cotovelo")
plt.show()


from sklearn.metrics import silhouette_score
inertias = []
silhouettes = []
ks = range(2, 9)

for k in ks:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = km.fit_predict(X_scaled)

    inertias.append(km.inertia_)
    silhouettes.append(silhouette_score(X_scaled, labels))

# Gráfico da silhueta
plt.figure(figsize=(8, 4))
plt.plot(ks, silhouettes, marker="o")
plt.xlabel("K")
plt.ylabel("Coeficiente de Silhueta")
plt.title("Método da Silhueta")
plt.show()


### Escolha do número de clusters (K = 4)

#Escolhi K = 4 para o modelo K-Means com base na análise do método do cotovelo e do silhouette score. No gráfico do cotovelo, observa-se uma redução significativa da inércia nos primeiros valores de K, com diminuição dos ganhos à medida que o número de clusters aumenta. Embora o silhouette score apresente seu maior valor em K = 2 (aproximadamente 0,418), K = 4 apresenta um resultado de aproximadamente 0,379, indicando uma qualidade de agrupamento razoável.#
#A escolha de quatro clusters busca equilibrar a qualidade da segmentação com a facilidade de interpretação dos resultados para o negócio. Com essa configuração, será possível investigar perfis mais específicos de clientes, considerando variáveis como limite de crédito, percentual de utilização e quantidade de atrasos nos últimos seis meses. Posteriormente, os grupos serão analisados para identificar suas características e comparar a proporção de clientes inadimplentes em cada perfil.


k_escolhido = 4  # exemplo
kmeans_final = KMeans(n_clusters=k_escolhido, random_state=42)
labels_kmeans = kmeans_final.fit_predict(X_scaled)

df_clean["cluster_kmeans"] = labels_kmeans
print(df_clean["cluster_kmeans"].value_counts().sort_index())
resumo_kmeans = df_clean.groupby("cluster_kmeans")[features].mean()
print(resumo_kmeans)
plt.scatter(
    df_clean["limite_credito"],
    df_clean["percentual_utilizacao_limite"],
    c=df_clean["cluster_kmeans"],
    alpha=0.7
)
plt.xlabel("Limite de crédito")
plt.ylabel("Uso do limite (%)")
plt.title("Clusters K-Means")
plt.show()




import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

# Criar a estrutura hierárquica
Z = linkage(X_scaled, method="ward")

# Plotar dendrograma
plt.figure(figsize=(14, 6))

dendrogram(
    Z,
    truncate_mode="lastp",
    p=30,
    leaf_rotation=90,
    leaf_font_size=9
)

plt.title("Dendrograma - HAC (Ward)")
plt.xlabel("Grupos de clientes")
plt.ylabel("Distância")
plt.show()




from sklearn.cluster import AgglomerativeClustering

k_escolhido = 4

hac = AgglomerativeClustering(
    n_clusters=k_escolhido,
    linkage="ward"
)

labels_hac = hac.fit_predict(X_scaled)

df_clean["cluster_hac"] = labels_hac

print("Quantidade de clientes por cluster HAC:")
print(df_clean["cluster_hac"].value_counts().sort_index())





import pandas as pd

comparacao = pd.crosstab(
    df_clean["cluster_kmeans"],
    df_clean["cluster_hac"],
    rownames=["K-Means"],
    colnames=["HAC"]
)

print(comparacao)





from sklearn.cluster import DBSCAN
import numpy as np

combinacoes = [
    (0.5, 5),
    (0.7, 5),
    (1.0, 5),
    (1.2, 5),
    (1.0, 10),
    (1.5, 5)
]

for eps, min_samples in combinacoes:
    dbscan = DBSCAN(
        eps=eps,
        min_samples=min_samples
    )

    labels = dbscan.fit_predict(X_scaled)

    n_clusters = len(set(labels) - {-1})
    n_ruido = np.sum(labels == -1)

    print(
        f"eps={eps}, min_samples={min_samples} | "
        f"Clusters: {n_clusters} | "
        f"Ruídos: {n_ruido}"
    )
dbscan = DBSCAN(
    eps=1.0,
    min_samples=5
)

labels_dbscan = dbscan.fit_predict(X_scaled)

df_clean["cluster_dbscan"] = labels_dbscan

print("\nDistribuição dos clusters DBSCAN:")
print(df_clean["cluster_dbscan"].value_counts().sort_index())

# Selecionar clientes classificados como ruído
anomalias = df_clean[
    df_clean["cluster_dbscan"] == -1
]

print("\nClientes classificados como ruído:")
print(
    anomalias[
        features + ["cluster_dbscan"]
    ]
)
df_clean["flag_inadimplente"] = df.loc[
    df_clean.index,
    "flag_inadimplente"
]

df_clean["tipo_dbscan"] = np.where(
    df_clean["cluster_dbscan"] == -1,
    "Ruído",
    "Cluster"
)

print(
    df_clean.groupby("tipo_dbscan")[
        features + ["flag_inadimplente"]
    ].mean().round(2)
)


### Comparação entre K-Means, HAC e DBSCAN
#O K-Means foi utilizado para segmentar os clientes em quatro grupos, enquanto o HAC foi aplicado com o mesmo número de clusters para permitir uma comparação entre os algoritmos. Os resultados mostraram distribuições diferentes, indicando que cada método identificou estruturas distintas nos dados. A tabela cruzada revelou algumas correspondências entre os grupos, mas também diferenças na organização dos clientes.#
#O DBSCAN foi utilizado para identificar regiões densas e possíveis pontos atípicos. Com os parâmetros `eps=1.0` e `min_samples=5`, foram encontrados quatro clusters e 12 clientes classificados como ruído, correspondendo a 4% da base analisada.#
#Um resultado relevante foi a proporção de inadimplentes entre os pontos classificados como ruído: aproximadamente 50%, em comparação com cerca de 16% entre os clientes agrupados. Esse resultado sugere uma possível associação entre perfis atípicos e maior risco de inadimplência. Entretanto, como o grupo de ruído contém apenas 12 clientes, essa observação deve ser interpretada com cautela e investigada em análises posteriores.