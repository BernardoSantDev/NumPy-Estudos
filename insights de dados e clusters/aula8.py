import numpy as np
import os
import matplotlib.pyplot as plt
os.environ["LOKY_MAX_CPU_COUNT"] = "4"

# Pontos em duas regiões densas + um ponto isolado
X = np.array([
    [1, 2], [1.1, 2.1], [0.9, 1.9], [1.2, 2.2],   # grupo A
    [5, 8], [5.1, 8.1], [4.9, 7.9], [5.2, 8.2],   # grupo B
    [10, 1]                                       # ponto isolado
])

plt.scatter(X[:, 0], X[:, 1])
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("Dados artificiais (antes do DBSCAN)")
plt.show()

#Aplicando DBSCAN
from sklearn.cluster import DBSCAN

# Escolha inicial de parâmetros
dbscan = DBSCAN(eps=0.5, min_samples=3)
labels = dbscan.fit_predict(X)

print("Rótulos dos pontos:", labels)



plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("Clusters com DBSCAN (labels: 0, 1, -1)")
plt.show()

dbscan_01 = DBSCAN(eps=0.1, min_samples=3)
labels_01 = dbscan_01.fit_predict(X)
print("Rótulos com eps=0.1:", labels_01)

dbscan_10 = DBSCAN(eps=1.0, min_samples=3)
labels_10 = dbscan_10.fit_predict(X)
print("Rótulos com eps=1.0:", labels_10)


#Com min_samples muito baixo, qualquer duplinha pode virar cluster.

dbscan_ms2 = DBSCAN(eps=0.5, min_samples=2)
labels_ms2 = dbscan_ms2.fit_predict(X)
print("Rótulos com min_samples=2:", labels_ms2)


