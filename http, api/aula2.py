import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
resposta = requests.get(url)

print("Status Code:", resposta.status_code)
print("Corpo da Resposta (texto):")
print(resposta.text)
