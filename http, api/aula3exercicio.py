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