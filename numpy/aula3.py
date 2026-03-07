import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10])
print(array)

print(array[0])
array[0] = 100
print(array)

#inserção
novo_array = np.insert(array, 2, 15)
print(novo_array)

#acrescimo
novo_array2 = np.append(array, 11)
print(novo_array2)
novo_array2 = np.append(array, [1,2,3])
print(novo_array2)

p1 = array[0:4]
p2 = array[4:10]
print(p1)
print(p2)
p3 = np.array([200])

resultado = np.concatenate((p1,p3,p2))
print(resultado)

#exclusão
novo_array3 = np.delete(array, 0)
print(novo_array3)

#operação de multiplicação
array_mult = array * 2
print(array_mult)
print(array*2)

#operação de soma
array_soma = array + 2
print(array_soma)
print(array+2)

#operaçao de classificação crescente
novo = array[::-1]
print(novo)
result = np.sort(novo)
print(result)

#operaçao de classificação decrescente
result_dec = -np.sort(-result)
print(result_dec)


