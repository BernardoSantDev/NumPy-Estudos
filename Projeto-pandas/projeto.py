import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('flights.csv')
print(df.head(10))
print(df.info())
print(df.isnull().sum())
print(df.describe().round(2))
print(df['Origin'].value_counts().head(10))

#unique() - util para identificar todos os valores sistindos em uma coluna de dados
#nunique() util para calcular a cardinalidade de um conjunto de dados, ou seja, quantos valores distintos existem
print(df['Origin'].unique())
print(df['Origin'].nunique())


#Cenario 1: extrair registros de voos apenas no ano 2000
df['Year'] = df['Fly Date'].astype(str).str.slice(0,4)
voos200 = df[df['Year'] == '2000']
print(voos200)

#Cenario 2: encontre voos que nao incluam LAX como origem
nox_lax = df[~df['Origin'].isin(['LAX'])]
print(nox_lax)

#Cenario 3: encontre voos que  incluam LAX como origem
lax = df[df['Origin'].isin(['LAX'])]
print(lax)

#Cenario 4: Mais de 100 passageiros e distancia < 1000 milhas
p_distancia = df[(df['Passengers']>100) & (df['Distance']<1000)]
print(p_distancia)

#Cenario 5: todos voos de/para NY ou LA
cidades = df[df['Origin City'].str.contains('New York|Los Angeles') 
            |df['Destination City'].str.contains('New York|Los Angeles')]
print(cidades)

#Cenario 6: Pop origem superios a 1 milhao
origem = df[(df['Origin Population']>1_000_000)]
print(origem)


#Cenario 7: Voos com assentos vazios
voos = df.query('Seats > Passengers')
print(voos)
print(voos['Destination City'])


#Cenario 8: voos com dist > 300 e com mais de 10 voos por mes
voosp = df.query('Distance < 300 & Flights > 10')
print(voosp)

# Salvando conjunto de ddos em algum cenatio
voosp.to_csv('vooslucrativos.csv')


#Cenario 1 agrupando por origem e destino
grouped = df.groupby(['Origin', 'Destination'])
#Aplica e agrega uma função ao grupo
aggregated = grouped.agg({'Passengers':'sum'})
#seleciona os valores dessa tabela
sorted_values = aggregated.sort_values(by='Passengers', ascending=False)
print(sorted_values.head())

grouped = df.groupby(['Origin', 'Destination'])
aggregated = grouped.agg({'Passengers':'sum', 'Flights':'sum'})
sorted_values = aggregated.sort_values(by=['Passengers', 'Flights'], ascending=False)
print(sorted_values.head())


#Cenario 2 agrupando por data de voo
#Convertendo fly date em datetime e criando mes para agrupamento
df['Month'] = pd.to_datetime(df['Fly Date'], format='%Y%m').dt.to_period('M')
# agrupar por mes e agregar soma a coluna voos
grouped = df.groupby('Month')
aggregated = grouped.agg({'Flights':'sum'})
#Classificando por mes
sorted_values = aggregated.sort_values(by='Month')
print(sorted_values)


#Colocaremos nossa coluna de distancia e definiremos nossos compartimentos conforme
#Teremos 0,500,1000,2000,3000,4000
#e para nosso compartimento final, desejaremos o maximo de nossa coluna de distancia para que nao aja nada apos esse compartimento

distance_bins = pd.cut(df['Distance'], bins=[0,500,1000,2000,3000,4000, df['Distance'].max()])


# Agrupe por intervalos de distancia e encontre o total de voos e passageiros para cada categoria de distancia
grouped_data = df.groupby(distance_bins).agg({'Flights':'sum', 'Passengers':'sum'})
sorted = grouped_data.sort_values(by='Distance', ascending=False)
print(sorted)



#Criando graficos
#Cenario 1 10 aeroportos de origem mais movimentados
#Agrupando por origem e agregando a soma dos voos
aeroportos = df.groupby('Origin').agg({'Flights':'sum'})
#Encontre os 10 aeroportos
aeroportos_p = aeroportos.nlargest(10, 'Flights')
#Plote os dados
aeroportos_p.plot(kind='bar')
plt.title('Aeroportos mais populares')
plt.ylabel('Número de voos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#Cenario 2: Agrupando por origem e destino
trafego = df.groupby(['Origin', 'Destination']).agg({'Passengers':'sum'})
#10 rotas com maior numero de passageiros 
rotaspopulares = trafego.nlargest(10, 'Passengers')
#Plote
rotaspopulares.plot(kind='bar', color='purple')
plt.title('As 10 rotas mais populares')
plt.ylabel('Número de passageiros')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#Cenario 1: Número de voos a cada ano
df['Year'] = df['Fly Date'].astype(str).str.slice(0, 4)
agrupa_ano = df.groupby('Year').agg({'Flights':'sum'})

#Plote
agrupa_ano.plot(kind='line')
plt.title('Total de voos por ano')
plt.xlabel('Ano')
plt.ylabel('Voos')
plt.xticks(rotation=45)
plt.show()


#Cenario 2: Agregando o numero de passaageiros por ano
p_ano = df.groupby('Year').agg({'Flights':'sum', 'Passengers':'sum'})
p_ano.plot(kind='line')
plt.title('Total de voos e passageiros por ano')
plt.xlabel('Ano')
plt.ylabel('Numero de Voos e passageiros')
plt.xticks(rotation=45)
plt.show()


#Cenario1 : Distribuição de voos por intervalo de distancia
distance_bins = pd.cut(df['Distance'], bins=[0,500,1000,2000,3000,4000, df['Distance'].max()])
distance_groups = df.groupby(distance_bins).agg({'Flights':'sum'})
#Plotagem
distance_groups.plot(kind='pie', y='Flights', title='Numero de voos por distancia')
plt.tight_layout()
plt.show()


