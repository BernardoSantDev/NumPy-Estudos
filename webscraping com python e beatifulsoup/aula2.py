import requests
from bs4 import BeautifulSoup

url = 'https://pt.wikipedia.org/wiki/Lista_de_monarcas_da_Inglaterra'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', class_='wikitable')
    if table:
        print('Tabela encontrada!')
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all(['th', 'td'])
            data = [cell.get_text(strip=True) for cell in cells]
            print(data)
    else:
        print('Tabela não encontrada')
else:
    print('Erro ao carregar pagina', response.status_code)


