import numpy as np

#convertendo
lista = [1,2,3,4,5]
array_l = np.array(lista)
print(array_l)

# valores especificos
zeros = np.zeros(5)
print(zeros)

one_array = np.ones(5)
print(one_array)

p_array = np.full((2,2), 5)
print(p_array)

# sequencias numericas
seq_array = np.arange(10)
print(seq_array)

linspace_array = np.linspace(0,1,5)
print(linspace_array)

#aleatorios
rand_array = np.random.rand(3,3)
print(rand_array)

rand_array = np.random.rand(5)
print(rand_array)