import numpy as np

matrix = np.matrix([[1,2,3], [4,5,6], [7,8,9]])
print(matrix)
print(matrix[1,2])

matrix[1,2] = 100
print(matrix)

print(matrix[1])
print(matrix[:,2])

print(matrix.size)
print(matrix.shape)

#encontrar indice de valor especifico
indice = np.where(matrix == 5)
print(indice)

#maximos e minimos
maximo = np.amax(matrix)
print(maximo)
minimo = np.amin(matrix)
print(minimo)

#verificação de condicionais
condicao = matrix > 5
print(condicao)
print("Tem alguem maior que 5?", np.any(condicao))
print("Todos sao maiores que 5?", np.all(condicao))