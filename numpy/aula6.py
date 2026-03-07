import numpy as np

matrix = np.matrix([[1,2,3],[4,5,6],[7,8,9]])

#add e remover linhas e colunas
#add linha = 0 | add coluna = 1
nova_linha = np.array([[10,20,30]])
matrix = np.append(matrix, nova_linha, axis=0)
print(matrix)

nova_coluna = np.array([[14], [14], [14], [14]])
matrix = np.append(matrix, nova_coluna, axis=1)
print(matrix)

#delete coluna = 1 | delete linha = 0
matrix = np.delete(matrix, 1, axis=1)
print(matrix)

matrix = np.delete(matrix, 3, axis=0)
print(matrix)


#redimensionamento
matrix = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
#convertendo de 3x3 para uma 2x2 usando reshape
array_np = np.asarray(matrix)
print(array_np)
#usamos o primeiro paramento, que é a nova forma desejada (2,2)
#usamos array_np.flattern()[:4] para considerar apenas os pimeiros 4 elementos
matriz_2x2 = array_np.flatten()[:4].reshape(2,2)
print(matriz_2x2)
