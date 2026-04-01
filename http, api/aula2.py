import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
resposta = requests.get(url)

print("Status Code:", resposta.status_code)
print("Corpo da Resposta (texto):")
print(resposta.text)

#convertendo para json

dados = resposta.json()
print("Tipo de 'dados':", type(dados))
print("Conteúdo de 'dados':" , dados)
print("Título do Post:", dados['title'])

#dados
print(resposta.status_code)
print(resposta.headers)
print(resposta.url)
print(resposta.text)
