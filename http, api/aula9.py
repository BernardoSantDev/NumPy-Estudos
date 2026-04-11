#Buscando e Convertendo XML para DataFrames com Pandas
import xml.etree.ElementTree as ET

xml_string = """
<catalogo>
  <livro id="1">
    <titulo>Introdução ao Python</titulo>
    <autor>Ana Silva</autor>
    <preco>79.90</preco>
    <ano>2020</ano>
  </livro>
  <livro id="2">
    <titulo>Data Science com Pandas</titulo>
    <autor>Bruno Souza</autor>
    <preco>99.50</preco>
    <ano>2022</ano>
  </livro>
  <livro id="3">
    <titulo>Machine Learning Prático</titulo>
    <autor>Carla Lima</autor>
    <preco>129.90</preco>
    <ano>2023</ano>
  </livro>
</catalogo>
"""

root = ET.fromstring(xml_string)

livros = []

for livro in root.findall("livro"):
    dados_livro = {
        "id": int(livro.attrib.get("id")),                         # atributo
        "titulo": livro.find("titulo").text.strip(),               # texto dentro da tag
        "autor": livro.find("autor").text.strip(),
        "preco": float(livro.find("preco").text),
        "ano": int(livro.find("ano").text),
    }
    livros.append(dados_livro)

print(livros)


#Transformando em DataFrame
import pandas as pd

df_livros = pd.DataFrame(livros)

print(df_livros)
print(df_livros.info())


#Exemplo com atributos mais ricos
#Extraindo atributos + elementos internos
import xml.etree.ElementTree as ET
import pandas as pd

xml_string = """
<produtos>
  <produto id="10" categoria="perifericos">
    <nome>Teclado Mecânico</nome>
    <preco>250.0</preco>
    <estoque>10</estoque>
  </produto>
  <produto id="20" categoria="perifericos">
    <nome>Mouse Gamer</nome>
    <preco>150.0</preco>
    <estoque>5</estoque>
  </produto>
</produtos>
"""

root = ET.fromstring(xml_string)

lista_produtos = []

for prod in root.findall("produto"):
    dados = {
        "id": int(prod.attrib.get("id")),
        "categoria": prod.attrib.get("categoria"),
        "nome": prod.find("nome").text.strip(),
        "preco": float(prod.find("preco").text),
        "estoque": int(prod.find("estoque").text)
    }
    lista_produtos.append(dados)

df_produtos = pd.DataFrame(lista_produtos)

print(df_produtos)
print(df_produtos.info())

#Exemplo com estrutura aninhada (XML mais complexo)
#Extraindo dados aninhados e somando
import xml.etree.ElementTree as ET
import pandas as pd

xml_string = """
<clientes>
  <cliente id="1">
    <nome>Ana</nome>
    <cidade>Juiz de Fora</cidade>
    <pedidos>
      <pedido valor="250.0" />
      <pedido valor="300.0" />
    </pedidos>
  </cliente>
  <cliente id="2">
    <nome>Bruno</nome>
    <cidade>São Paulo</cidade>
    <pedidos>
      <pedido valor="150.0" />
    </pedidos>
  </cliente>
</clientes>
"""

root = ET.fromstring(xml_string)

clientes_resumo = []

for cli in root.findall("cliente"):
    id_cliente = int(cli.attrib.get("id"))
    nome = cli.find("nome").text.strip()
    cidade = cli.find("cidade").text.strip()

    # pegar todos os pedidos desse cliente
    pedidos = cli.findall("pedidos/pedido")

    # somar os valores
    valores = []
    for p in pedidos:
        valor_str = p.attrib.get("valor")
        valores.append(float(valor_str))

    total_pedidos = sum(valores)
    qtde_pedidos = len(valores)

    clientes_resumo.append({
        "id": id_cliente,
        "nome": nome,
        "cidade": cidade,
        "qtde_pedidos": qtde_pedidos,
        "total_pedidos": total_pedidos
    })

df_clientes = pd.DataFrame(clientes_resumo)

print(df_clientes)


#Pequena limpeza com pandas
#Depois de transformar o XML em DataFrame, vale revisar:
#Tipos (df.dtypes)
#Valores nulos (df.isna().sum())
#Nomes de colunas (se estão claros, sem caracteres estranhos)
print(df_clientes.info())

# renomear colunas para algo mais amigável (se quiser)
df_clientes = df_clientes.rename(columns={
    "qtde_pedidos": "quantidade_pedidos",
    "total_pedidos": "valor_total_pedidos"
})

print(df_clientes.head())










