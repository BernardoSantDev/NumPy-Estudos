import numpy as np

array = np.arange(0,11)
print(array)

primeiro = array[0]
print(primeiro)

ultimo = array[-1]
print(ultimo)


p_cinco = array[:5]
print(p_cinco)

c_ediante = array[5:]
print(c_ediante)

ar = ['a','b','c','d','e', 'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t']
print(ar[0:5])
print(ar[5:])
print(ar[8::2])
print(ar[12::-2])

ar_t = np.array(ar)
print(ar_t.size)

array = np.arange(0,11)
#max
print(np.amax(array))
#min
print(np.amin(array))
#media
print(np.mean(array))
print(np.average(array))
#desvio padrao
print(np.std(array))