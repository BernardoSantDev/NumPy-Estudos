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

t2 = table[2]
print('Segunda tabela encontrada!')
rows = t2.find_all('tr')
for row in rows:
    cells = row.find_all(['th', 'td'])
    data = [cell.get_text(strip=True) for cell in cells]
    print(data)

monarcas = []

for row in rows:
    cells = row.find_all(['th', 'td'])
    if len(cells) == 6:
        monarca = {
            'Nome': cells[0].get_text(strip=True),
            'Retrato': cells[1].find('img')['src'] if cells[1].find('img') else 'N/A',
            'Nascimento': cells[2].get_text(strip=True),
            'Casamento(s)': cells[3].get_text(strip=True),
            'Morte': cells[4].get_text(strip=True),
            'Ref': cells[5].get_text(strip=True)
        }
        monarcas.append(monarca)

for monarca in monarcas:
    print(monarca)
