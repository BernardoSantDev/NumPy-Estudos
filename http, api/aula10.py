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




















