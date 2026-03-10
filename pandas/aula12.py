import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


a = np.random.randn(100)
b = np.random.randn(100)


df = pd.DataFrame({'A':a, 'B':b})
df.plot(kind='scatter', x='A', y='B', title='Grafico de dispersão de A vs B')
plt.xlabel('Valor de A')
plt.ylabel('Valor de B')
plt.tight_layout()
plt.show()

a = np.random.randn(100)
b = a * 2 + np.random.randn(100)*0.5

df = pd.DataFrame({'A':a, 'B':b})
df.plot(kind='scatter', x='A', y='B', title='Grafico de dispersão de A vs B')
plt.xlabel('Valor de A')
plt.ylabel('Valor de B')
plt.tight_layout()
plt.show()











