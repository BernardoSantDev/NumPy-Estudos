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


#Estratégias de chave de junção
#A chave de junção é a coluna que “liga” as tabelas.

#Casos comuns:

#IDs numéricos (id_cliente, id_cidade, id_produto).
#Nomes (cidade, estado, categoria).
#Códigos oficiais (IBGE, SKU, ISO, etc.).
#Boas práticas:
#Prefira IDs estáveis (códigos numéricos ou strings únicas).
#Evite depender só de nome (pode ter variações de grafia, acentos, maiúsculas/minúsculas).
#Quando for usar nome, tente padronizar:
#str.strip() (tirar espaços).
#str.title() ou str.upper() (padronizar caixa).
#No nosso exemplo, vamos usar a coluna "cidade" como chave, mas com cuidado.

#6. Tratando discrepâncias nas chaves
#Problemas típicos:

#Nome escrito de formas diferentes:
#"sao paulo", "São Paulo", "SÃO PAULO".
#Espaços extras:
#"Juiz de Fora " vs "Juiz de Fora".
#Cidades presentes no CSV e ausentes na API (ou vice-versa).
#6.1 Padronização simples
#Antes do merge, podemos:
## Padronizar nome da cidade nas duas tabelas
df_clima["cidade"] = df_clima["cidade"].str.strip().str.title()
df_metas["cidade"] = df_metas["cidade"].str.strip().str.title()
#Assim:
#"São Paulo", "SÃO PAULO", " sao paulo " → "São Paulo"

#6.2 Fazendo o merge
df_integrado = pd.merge(
    df_metas,
    df_clima,
    on="cidade",
    how="left"    # mantemos todas as cidades do CSV
)

print(df_integrado)



#7. Lidando com dados faltantes pós-merge
#Depois do merge, você precisa decidir o que fazer com colunas que vieram com NaN:

#Eles significam:
#Não existe informação naquela fonte para aquela chave.
#Erro de digitação / chave não bateu.
#7.1 Estratégias possíveis
#Remover linhas sem dados complementares:
df_sem_nan = df_integrado.dropna(subset=["temp_atual"])
#Preencher com valor padrão:
#Ex: 0, "Desconhecido", média, etc.
df_integrado["temp_atual"] = df_integrado["temp_atual"].fillna(-999)
#Investigar manualmente:
#Pode ser que o problema seja no cadastro (nome errado, cidade não coberta pela API, etc.).
#No nosso exemplo, pode fazer sentido manter Belo Horizonte, mas marcar que não temos clima para ela.



#8. Prática guiada da aula (roteiro sugerido)
#8.1 Passo 1 – Consumir uma API e obter um DataFrame principal
#Sugestões de APIs públicas (para o professor/aluno escolher, dependendo do ambiente):
#
#API de clima (OpenWeatherMap – requer chave gratuita).
#API de criptomoedas (CoinGecko, etc.).
#API de filmes (OMDb – requer chave).
#API de teste JSONPlaceholder (posts, users, etc.).
#Para simplificar o material, vamos usar um exemplo “genérico” de clima com requests (o código é ilustrativo, pode ser adaptado para qualquer API):
#
import requests
import pandas as pd
API_KEY = "SUA_CHAVE_AQUI"  # ideal: usar variável de ambiente
cidades = ["Juiz de Fora", "São Paulo", "Rio de Janeiro"]

dados_clima = []

for cidade in cidades:
    params = {
        "q": cidade,
        "appid": API_KEY,
        "units": "metric",   # temperatura em Celsius
        "lang": "pt_br"
    }
    resposta = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
    resposta.raise_for_status()
    json_data = resposta.json()

    dados_clima.append({
        "cidade": cidade,
        "temp_atual": json_data["main"]["temp"],
        "umidade": json_data["main"]["humidity"]
    })

df_clima = pd.DataFrame(dados_clima)
print(df_clima)
#8.2 Passo 2 – Ler um CSV local com informações complementares
#Exemplo: cidades_metas.csv (criadas pelo professor):

#cidade,regiao,populacao,meta_vendas
#Juiz de Fora,Sudeste,573285,50000
#São Paulo,Sudeste,12300000,300000
#Rio de Janeiro,Sudeste,6718903,200000
#Belo Horizonte,Sudeste,2521564,150000
#Leitura:

df_metas = pd.read_csv("cidades_metas.csv")
print(df_metas)

#8.3 Passo 3 – Padronizar chave de junção
df_clima["cidade"] = df_clima["cidade"].str.strip().str.title()
df_metas["cidade"] = df_metas["cidade"].str.strip().str.title()
#8.4 Passo 4 – Integrar com merge
df_final = pd.merge(
    df_metas,
    df_clima,
    on="cidade",
    how="left"   # mantém todas as cidades do CSV
)

#print(df_final)
#8.5 Passo 5 – Gerar um “relatório” simples
#Exemplos de perguntas para os alunos responderem a partir do df_final:

#Quais cidades têm dados de clima disponíveis?
print(df_final[["cidade", "temp_atual"]])
#Qual cidade tem maior meta de vendas?
print(df_final.sort_values("meta_vendas", ascending=False).head(1))
#Qual a média da temperatura nas cidades com meta acima de X?
filtro = df_final["meta_vendas"] > 100000
media_temp = df_final.loc[filtro, "temp_atual"].mean()
print("Média de temperatura nas cidades com alta meta:", media_temp)
#(Opcional) Gerar um gráfico simples: meta de vendas vs temperatura.
import matplotlib.pyplot as plt

df_plot = df_final.dropna(subset=["temp_atual"])

plt.scatter(df_plot["temp_atual"], df_plot["meta_vendas"])
plt.xlabel("Temperatura atual (°C)")
plt.ylabel("Meta de vendas")
plt.title("Meta de vendas x Temperatura")
plt.show()






















































