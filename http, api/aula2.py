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

#enviar parametros
import requests

url = "https://jsonplaceholder.typicode.com/comments"

parametros = {
    "postId": 1  # queremos comentários apenas do post com id=1
}

resposta = requests.get(url, params=parametros)

print("URL final:", resposta.url)  # veja como ficou a query string
print("Status code:", resposta.status_code)

comentarios = resposta.json()
print("Quantidade de comentários retornados:", len(comentarios))
print("Primeiro comentário:", comentarios[0])
