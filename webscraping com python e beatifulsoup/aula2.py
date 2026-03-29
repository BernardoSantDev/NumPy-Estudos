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
    print('Tabela não encontrada')
    
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find_all('table', class_='wikitable')
if len(table) > 1:
    t2 = table[1]
    print('Segunda tabela encontrada!')
    rows = t2.find_all('tr')
    for row in rows:
        cells = row.find_all(['th', 'td'])
        data = [cell.get_text(strip=True) for cell in cells]
        print(data)
else:
    print('Erro ao carregar pagina', response.status_code)


