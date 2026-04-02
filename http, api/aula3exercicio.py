import requests

usuarios = [
    {"id": 1, "nome": "Ana",   "idade": 28, "cidade": "Juiz de Fora"},
    {"id": 2, "nome": "Bruno", "idade": 22, "cidade": "São Paulo"},
    {"id": 3, "nome": "Carla", "idade": 31, "cidade": "Rio de Janeiro"},
    {"id": 4, "nome": "Diego", "idade": 19, "cidade": "Juiz de Fora"}
]

for item in usuarios:
    nome = item["nome"]
    idade = item["idade"]
    cidade = item["cidade"]

    print(f"{nome} ({idade} anos) - {cidade}")

usuarios_jf = [u for u in usuarios if u["cidade"] == "Juiz de Fora"]
print(usuarios_jf)

print(f"Juiz de Fora moram {len(usuarios_jf)} pessoas.")
for u in usuarios_jf:
    nomejf = u["nome"]
    print(f"Nome: {nomejf}")

print(f"Juiz de Fora moram {len([u for u in usuarios if u['cidade'] == 'Juiz de Fora'])} pessoas.")

for u in usuarios:
    if (u["cidade"] == "Juiz de Fora"):
        print(u["nome"])


loja = {
    "nome": "Codi Tech Store",
    "produtos": [
        {
            "id": 1,
            "nome": "Notebook",
            "preco": 3500.0,
            "categorias": ["eletrônicos", "computadores"],
            "disponivel": True
        },
        {
            "id": 2,
            "nome": "Headset Gamer",
            "preco": 300.0,
            "categorias": ["eletrônicos", "áudio"],
            "disponivel": False
        },
        {
            "id": 3,
            "nome": "Webcam Full HD",
            "preco": 200.0,
            "categorias": ["eletrônicos", "vídeo"],
            "disponivel": True
        }
    ]
}




print(f'O nome da loja é {loja['nome']}')


print("\n Lista de Itens")
for item in loja["produtos"]:
    nome = item["nome"]
    preco = item["preco"]
    estoque = item["disponivel"]

    status_estoque = "Disponivel" if estoque == True else "Indisponivel"
    
    print(f" - {nome} - R${preco:.2f} - {status_estoque}")
    
produtos_disponiveis = [p['nome'] for p in loja["produtos"] if p["disponivel"] == True]
print(produtos_disponiveis)


# Calcule o preço médio dos produtos disponíveis

precos_disponiveis = [p['preco'] for p in loja["produtos"] if p["disponivel"] == True]
if len(precos_disponiveis) > 0:
    preco_medio = sum(precos_disponiveis) / len(precos_disponiveis)
    print(f"Preço médio dos produtos disponíveis: R${preco_medio:.2f}")

