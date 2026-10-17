import numpy as np
import matplotlib.pyplot as plt

# Cada linha é [qtd_compras, valor_medio]
X = np.array([
    [1, 50], [2, 45], [1, 60],       # Grupo 1: poucos pedidos, ticket baixo
    [10, 200], [12, 220], [9, 180],  # Grupo 2: vários pedidos, ticket médio
    [4, 500], [5, 550], [6, 600]     # Grupo 3: poucos pedidos, ticket alto
])

plt.scatter(X[:, 0], X[:, 1])
plt.xlabel("Quantidade de compras no mês")
plt.ylabel("Ticket médio (R$)")
plt.title("Clientes em um espaço 2D")
plt.show()


#6.1. K-Means
#Você escolhe um número de grupos K (ex: 3 clusters).
#O algoritmo tenta posicionar K centróides de modo que cada ponto fique próximo de um deles.
#No fim, cada ponto pertence ao cluster do centróide mais próximo.
#Use K-Means quando:
#Quer segmentar clientes em um número fixo de grupos (ex: 3 perfis principais).
#Seus dados são relativamente “bem comportados” (sem clusters com formas muito estranhas).
#Você vai ver:
#Como rodar K-Means com scikit-learn.
#Como escolher K (método do cotovelo).
#Como interpretar os clusters.

#6.2. DBSCAN
#Não precisa escolher K.
#Ele agrupa pontos que estão densamente próximos, e marca pontos isolados como ruído (-1).
#É útil quando:
#Você desconfia que há outliers/anomalias.
#Os clusters podem ter formatos estranhos (não só “bolas”).
#Você vai ver:
#Como ajustar os parâmetros eps e min_samples.
#Como interpretar pontos marcados como ruído.
#Exemplos de detecção de comportamento “estranho”.

#6.3. HAC (Hierarchical Agglomerative Clustering)
#Pensa em clusters de forma hierárquica:
#começa com tudo separado e vai juntando os pontos/grupos mais próximos.
#O resultado pode ser visualizado em um dendrograma (uma espécie de árvore).
#É útil quando:
#Você quer enxergar diferentes níveis de agrupamento (por exemplo, 2 grandes grupos que se subdividem em grupos menores).
#Você quer uma visão “de cima” da similaridade entre observações.
#Você vai ver:
#Como rodar HAC com scikit-learn.
#Como ler um dendrograma.
#Como comparar HAC com K-Means.


