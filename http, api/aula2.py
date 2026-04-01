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


#Tratamento de erros
#TRATAMENTO1
url = "https://jsonplaceholder.typicode.com/posts/1"
resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    print("Título:", dados["title"])
else:
    print("Falha ao buscar dados. Código:", resposta.status_code)


#TRATAMENTO2
url = "https://jsonplaceholder.typicode.com/posts/1"
resposta = requests.get(url)

try:
    resposta.raise_for_status()  # se não for 2xx, lança erro
    dados = resposta.json()
    print("Título:", dados["title"])
except requests.exceptions.HTTPError as e:
    print("Ocorreu um erro HTTP:", e)


#TRATAMENTO3

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    resposta = requests.get(url, timeout=5)  # espera no máximo 5 segundos
    resposta.raise_for_status()
    dados = resposta.json()
    print("Título:", dados["title"])
except requests.exceptions.Timeout:
    print("A requisição demorou demais e foi cancelada (timeout).")
except requests.exceptions.RequestException as e:
    print("Erro ao fazer requisição:", e)

