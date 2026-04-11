#Lendo JSON e XML de Arquivos Locais e Integrando Múltiplas Fontes


#Usando json (para ter controle total)
import json

with open("vendas.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

print(type(dados))  # deve ser list
print(dados)
import pandas as pd

df_vendas = pd.DataFrame(dados)
print(df_vendas)

#Usando pandas.read_json direto
import pandas as pd

df_vendas = pd.read_json("vendas.json")
print(df_vendas)
print(df_vendas.info())
#Você também pode ler JSON de string:

json_string = '[{"id": 1, "nome": "Ana"}, {"id": 2, "nome": "Bruno"}]'
df = pd.read_json(json_string)




#Lendo XML de arquivo local
#Lendo com ET.parse
import xml.etree.ElementTree as ET

tree = ET.parse("catalogo.xml")  # carrega o arquivo
root = tree.getroot()           # obtém tag raiz

print(root.tag)  # 'catalogo'
#Transformando em lista de dicionários e DataFrame
import pandas as pd

livros = []

for livro in root.findall("livro"):
    dados_livro = {
        "id": int(livro.attrib.get("id")),
        "titulo": livro.find("titulo").text.strip(),
        "autor": livro.find("autor").text.strip(),
        "preco": float(livro.find("preco").text)
    }
    livros.append(dados_livro)

df_livros = pd.DataFrame(livros)
print(df_livros)
#Arquivo XML local → ET.parse → root → lista de dicionários → pd.DataFrame.



#Lendo CSV de arquivo local

import pandas as pd

df_csv = pd.read_csv("vendas.csv")
print(df_csv)
print(df_csv.info())
#Se o separador for ;:
df_csv = pd.read_csv("vendas_ponto_virgula.csv", sep=";")
#Se precisar especificar encoding:
df_csv = pd.read_csv("vendas.csv", encoding="utf-8")



#Exemplo de integração: API + CSV
#Cenário realista:
#Você tem dados novos de vendas vindos de uma API em JSON.
#Você tem um arquivo antigo vendas_anteriores.csv local.
#Quer juntar tudo em um único DataFrame.
#Supor dados da API (já em DataFrame)
import pandas as pd

# Dados "novos" (por exemplo, vieram de uma API agora e você já transformou em DataFrame)
dados_novos = [
    {"id_venda": 4, "produto": "Cadeira Gamer", "valor": 1200.0},
    {"id_venda": 5, "produto": "Monitor 24\"",  "valor": 900.0}
]
df_novos = pd.DataFrame(dados_novos)
#Ler CSV antigo
df_antigos = pd.read_csv("vendas_anteriores.csv")
#Juntar linhas com pd.concat
#Quando os dados têm as mesmas colunas e você quer “empilhar”, use concat.
df_todos = pd.concat([df_antigos, df_novos], ignore_index=True)
print(df_todos)
#ignore_index=True recria o índice (0, 1, 2…).
#Agora você tem histórico + novos dados no mesmo DataFrame.



#Exemplo de integração: JSON + XML (relacionando por chave)
#Outro cenário bem comum:
#Um arquivo JSON com cadastros de clientes.
#Um arquivo XML com pedidos que referenciam esses clientes por um id_cliente.

#Clientes em JSON → DataFrame
import pandas as pd

df_clientes = pd.read_json("clientes.json")
print(df_clientes)

# Pedidos em XML → DataFrame

import xml.etree.ElementTree as ET
import pandas as pd

tree = ET.parse("pedidos.xml")
root = tree.getroot()

lista_pedidos = []

for p in root.findall("pedido"):
    lista_pedidos.append({
        "id_pedido": int(p.attrib.get("id")),
        "id_cliente": int(p.attrib.get("id_cliente")),
        "valor": float(p.attrib.get("valor"))
    })

df_pedidos = pd.DataFrame(lista_pedidos)
print(df_pedidos)

#Agora temos:
#df_clientes: info dos clientes.
#df_pedidos: info dos pedidos (com id_cliente).

#7.3 Integrando com pd.merge (JOIN)
#Queremos um DataFrame com:
#nome do cliente
#cidade
#id do pedido
#valor
#Isso é um join: unir tabelas pelo campo em comum id_cliente.

df_completo = pd.merge(
    df_pedidos,
    df_clientes,
    on="id_cliente",      # coluna em comum nas duas tabelas
    how="left"            # tipo de join
)

print(df_completo)

#Tipo de join:
#how="inner" → só linhas que existem nos dois lados.
#how="left" → todas as linhas de df_pedidos, preenchendo cliente onde houver correspondência.
#how="right" → todas de df_clientes.
#how="outer" → união de todos, preenchendo com NaN onde não houver match.
#No nosso caso left faz sentido, pois:
#Para cada pedido, queremos trazer os dados do cliente (se existir).
#Agora você consegue:
#Agrupar por nome para ver total de pedidos.
#Agrupar por cidade.
#Calcular ticket médio por cliente.




#8. Integrando várias fontes: mini projeto
#Imagine o cenário:

#Você tem:
#clientes.json (cadastro de clientes).
#pedidos_api.json (novos pedidos da API).
#pedidos_antigos.xml (pedidos antigos num XML legado).
#Quer gerar um único DataFrame com todos os pedidos + info dos clientes.
#Fluxo (simplificado):

#Clientes:
#Ler clientes.json → df_clientes.
#Pedidos novos (JSON):
#Ler pedidos_api.json → df_novos.
#Pedidos antigos (XML):
#Ler pedidos_antigos.xml com ET.parse.
#Transformar em lista de dicionários → df_antigos.
#Juntar pedidos:
#df_pedidos = pd.concat([df_novos, df_antigos], ignore_index=True).
#Relacionar com clientes:
#df_completo = pd.merge(df_pedidos, df_clientes, on="id_cliente", how="left").
#Analisar / salvar:
#Agrupar por cliente, por cidade, etc.
#Salvar em relatorio_pedidos_completo.csv.
#Esse padrão de projeto é muito comum em Data Science / Engenharia de Dados.

