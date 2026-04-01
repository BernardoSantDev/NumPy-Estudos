import requests

url = "https://jsonplaceholder.typicode.com/comments"
resposta = requests.get(url)

dados = resposta.json()
print(resposta.status_code)
print(resposta.text[:5000])