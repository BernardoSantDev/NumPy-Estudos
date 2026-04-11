# Integrando Múltiplas Fontes de Dados (APIs + Arquivos)

#2. Por que integrar múltiplas fontes?
#Na prática, quase nenhum projeto de Data Science vive só de uma fonte única. Exemplos reais:

#API de clima → dados de temperatura atual por cidade
#CSV local → tabela de cidades, população, região, meta de vendas
#Sozinha, a API mostra o clima.
#Sozinho, o CSV mostra suas metas.
#Juntos, você consegue responder perguntas como:

#“Existe relação entre clima e venda de certo produto?”
#“Como está a meta de vendas nas cidades com maior variação de temperatura?”
#Integração de dados é o que transforma um monte de tabelas espalhadas em um painel coerente de informações.

#3. Revisão rápida: merge e joins no pandas
#O merge do pandas faz exatamente o que um “JOIN” de banco de dados faz.

#3.1 Exemplo simples
import pandas as pd

df_clientes = pd.DataFrame({
    "id_cliente": [1, 2, 3],
    "nome": ["Ana", "Bruno", "Carla"]
})

df_pedidos = pd.DataFrame({
    "id_pedido": [10, 11, 12],
    "id_cliente": [1, 1, 3],
    "valor": [250.0, 300.0, 150.0]
})

df_merged = pd.merge(df_pedidos, df_clientes, on="id_cliente", how="inner")
print(df_merged)

#3.2 Tipos de join (how)
#inner (padrão):
#Só mantém linhas que existem nas duas tabelas.
#left:
#Mantém todas as linhas da tabela da esquerda, preenchendo com NaN o que não existir na direita.
#right:
#Mantém todas as linhas da tabela da direita.
#outer:
#Junta tudo de ambos os lados, preenchendo NaN quando não houver correspondência.
#Visualmente (simplificando):

#inner → interseção
#left → tudo da esquerda, mais o que bater da direita
#outer → união de tudo

#4. Exemplo de cenário: API + CSV local
#Vamos montar um cenário didático:

#API (simulada): retorna temperatura atual por cidade.
#CSV local: contém cidades com população e meta de vendas.
#4.1 Dados da “API” (simulados)
#Imagine que você fez uma requisição a uma API de clima e obteve algo assim (já convertido para DataFrame):

import pandas as pd

df_clima = pd.DataFrame([
    {"cidade": "Juiz de Fora", "temp_atual": 24.5},
    {"cidade": "São Paulo",    "temp_atual": 19.0},
    {"cidade": "Rio de Janeiro","temp_atual": 27.3},
])
print(df_clima)

#4.2 CSV local com metas (simulado)
#Suponha um CSV metas_cidades.csv com:

#cidade,regiao,populacao,meta_vendas
#Juiz de Fora,Sudeste,573285,50000
#São Paulo,Sudeste,12300000,300000
#Rio de Janeiro,Sudeste,6718903,200000
#Belo Horizonte,Sudeste,2521564,150000
#Lendo no pandas:

df_metas = pd.read_csv("metas_cidades.csv")
print(df_metas)
































































