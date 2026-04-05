#Introdução a XML: Conceitos e Leitura com Python
#Ele é uma linguagem de marcação (como o HTML) usada para representar dados de forma hierárquica.

#Exemplo de JSON:
#{
#  "id": 1,
#  "nome": "Ana",
#  "idade": 28
#}
#Exemplo equivalente em XML:

#<usuario>
#  <id>1</id>
#  <nome>Ana</nome>
#  <idade>28</idade>
#</usuario>


#Lendo XML em Python com xml.etree.ElementTree
#O Python já vem com uma biblioteca padrão para XML:
#import xml.etree.ElementTree as ET

import xml.etree.ElementTree as ET

xml_string = """
<catalogo>
  <livro id="1">
    <titulo>Introdução ao Python</titulo>
    <autor>Ana Silva</autor>
    <preco>79.90</preco>
  </livro>
  <livro id="2">
    <titulo>Data Science com Pandas</titulo>
    <autor>Bruno Souza</autor>
    <preco>99.50</preco>
  </livro>
</catalogo>
"""

# Converte string em árvore XML
root = ET.fromstring(xml_string)

print(root)          # objeto Element
print(root.tag)      # nome da tag raiz: 'catalogo'


#Iterando sobre elementos filhos
#Queremos percorrer todos os <livro> dentro de <catalogo>:
for livro in root:
    print(livro.tag, livro.attrib)



#Acessando texto de elementos internos
for livro in root:
    id_livro = livro.attrib.get("id")

    titulo = livro.find("titulo").text
    autor = livro.find("autor").text
    preco = livro.find("preco").text

    print(f"ID: {id_livro} | {titulo} - {autor} (R${preco})")




#Lendo XML de um arquivo
#Usando ET.parse
import xml.etree.ElementTree as ET

tree = ET.parse("catalogo.xml")  # carrega o arquivo
root = tree.getroot()            # obtém o elemento raiz

print(root.tag)  # deve mostrar: catalogo
for livro in root:
    titulo = livro.find("titulo").text
    print(titulo)




#Navegando com find e findall
#find – pega o primeiro que bater
primeiro_livro = root.find("livro")
print(primeiro_livro.attrib)

#findall – pega todos os que batem
todos_livros = root.findall("livro")
print("Quantidade de livros:", len(todos_livros))

for livro in todos_livros:
    print(livro.attrib)


#Suponha um XML assim:
#
#<loja>
#  <endereco>
#    <cidade>Juiz de Fora</cidade>
#    <estado>MG</estado>
#  </endereco>
#  <produtos>
#    <produto>...</produto>
#    <produto>...</produto>
#  </produtos>
#</loja>
#Você poderia fazer:

cidade = root.find("endereco/cidade").text
print(cidade)  # Juiz de Fora

produtos = root.findall("produtos/produto")






#Transformando XML em estruturas Python (lista de dicionários)
import xml.etree.ElementTree as ET

xml_string = """
<catalogo>
  <livro id="1">
    <titulo>Introdução ao Python</titulo>
    <autor>Ana Silva</autor>
    <preco>79.90</preco>
  </livro>
  <livro id="2">
    <titulo>Data Science com Pandas</titulo>
    <autor>Bruno Souza</autor>
    <preco>99.50</preco>
  </livro>
</catalogo>
"""

root = ET.fromstring(xml_string)

livros = []

for livro in root.findall("livro"):
    dados_livro = {
        "id": livro.attrib.get("id"),
        "titulo": livro.find("titulo").text,
        "autor": livro.find("autor").text,
        "preco": float(livro.find("preco").text)
    }
    livros.append(dados_livro)

print(livros)