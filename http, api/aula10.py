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











