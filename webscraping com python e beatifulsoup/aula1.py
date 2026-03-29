import requests
from bs4 import BeautifulSoup

url = 'https://pt.wikipedia.org/wiki/Lista_de_monarcas_da_Inglaterra'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print('Pagina carregada com sucesso!')
else:
    print('Erro ao carregar pagina', response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())





