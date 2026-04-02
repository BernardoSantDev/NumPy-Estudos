import requests

dados ={
  "id": 101,
  "nome": "Ana",
  "idade": 30,
  "ativo": True
}

print(dados["nome"])   # Ana
print(dados["idade"])  # 30
print(dados["ativo"])  # True


print(dados.get("nome"))          # Ana
print(dados.get("profissao"))     # None (não existe, não dá erro. DA NONE)
print(dados.get("profissao", "N/A"))  # N/A (valor padrão)

usuarios = [
    {"id": 1, "nome": "Ana",   "idade": 30},
    {"id": 2, "nome": "Bruno", "idade": 25},
    {"id": 3, "nome": "Carla", "idade": 35}
]


primeiro = usuarios[0]   # dicionário da Ana
segundo  = usuarios[1]   # dicionário do Bruno

print(primeiro)          # {'id': 1, 'nome': 'Ana', 'idade': 30}
print(primeiro["nome"])  # Ana
print(segundo["idade"])  # 25

for usuario in usuarios:
    print("ID:", usuario["id"], "- Nome:", usuario["nome"])


cidade = {
    "nome": "Juiz de Fora",
    "estado": "MG",
    "populacao": 573285,
    "coordenadas": {
        "latitude": -21.7642,
        "longitude": -43.3496
    }
}

print(cidade["nome"])  # Juiz de Fora

coord = cidade["coordenadas"]
print(coord)           # {'latitude': -21.7642, 'longitude': -43.3496}

print(coord["latitude"])   # -21.7642
print(cidade["coordenadas"]["longitude"])  # -43.3496 (acesso direto, encadeado)


resposta_api = {
    "pagina": 1,
    "total_paginas": 5,
    "usuarios": [
        {"id": 1, "nome": "Ana"},
        {"id": 2, "nome": "Bruno"},
        {"id": 3, "nome": "Carla"}
    ]
}

usuarios = resposta_api["usuarios"]
print(type(usuarios))  # <class 'list'>
print(usuarios)

for u in usuarios:
    print("ID:", u["id"], "- Nome:", u["nome"])

for i, u in enumerate(usuarios):
    print(f"Posição {i} na lista -> ID: {u['id']} - Nome: {u['nome']}")


filme = {
    "titulo": "Matrix",
    "ano": 1999,
    "elenco": [
        {"ator": "Keanu Reeves", "personagem": "Neo"},
        {"ator": "Laurence Fishburne", "personagem": "Morpheus"},
        {"ator": "Carrie-Anne Moss", "personagem": "Trinity"}
    ],
    "avaliacoes": {
        "imdb": 8.7,
        "rotten_tomatoes": 88
    }
}

print(filme["titulo"])  # Matrix
print(filme["avaliacoes"]["imdb"])  # 8.7

for membro in filme["elenco"]:
    print(membro["ator"], "->", membro["personagem"])



#EXEMPLO COMPLETO simulando resposta de API

resposta_api = {
    "loja": "Tech Store",
    "cidade": "São Paulo",
    "itens": [
        {"id": 1, "nome": "Teclado Mecânico", "preco": 250.0, "estoque": 10},
        {"id": 2, "nome": "Mouse Gamer",      "preco": 150.0, "estoque": 0},
        {"id": 3, "nome": "Monitor 24\"",     "preco": 900.0, "estoque": 5}
    ]
}


print("Loja:", resposta_api["loja"])
print("Cidade:", resposta_api["cidade"])

print("\nLista de itens:")
for item in resposta_api["itens"]:
    nome = item["nome"]
    preco = item["preco"]
    estoque = item["estoque"]

    # Texto mais amigável
    status_estoque = "disponível" if estoque > 0 else "sem estoque"

    print(f"- {nome} | R${preco:.2f} | {status_estoque}")