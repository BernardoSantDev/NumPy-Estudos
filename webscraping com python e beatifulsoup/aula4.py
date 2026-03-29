import requests
from bs4 import BeautifulSoup
import re

url = 'https://pt.wikipedia.org/wiki/Lista_de_monarcas_da_Inglaterra'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.find_all('table', class_='wikitable')

t2 = tables[2]

rows = t2.find_all('tr')

monarchs = []

def clean_name(name):
    return re.split(r'\d', name)[0].strip()

def clean_birthdate(birthdate):
    match = re.match(r'^\d+', birthdate)
    return match.group() if match else birthdate

# Função para limpar o campo "Casamento(s)"
def clean_marriage(marriage):
    # Remove números (ex: "2 filhos", "19 filhos")
    cleaned = re.sub(r'\d+', '', marriage)
    # Remove a palavra "filho" ou "filhos"
    cleaned = re.sub(r'\bfilhos?\b', '', cleaned, flags=re.IGNORECASE)
    # Remove espaços extras
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned


for row in rows[1:]:  # ignora cabeçalho
    cells = row.find_all(['th', 'td'])

    if len(cells) == 6:
        nome_completo = cells[0].get_text(strip=True)
        nascimento_completo = cells[2].get_text(strip=True)
        casamento_completo = cells[3].get_text(strip=True)

        monarch = {
            'Nome': clean_name(nome_completo),
            'Retrato': cells[1].find('img')['src'] if cells[1].find('img') else 'N/A',
            'Nascimento': clean_birthdate(nascimento_completo),
            'Casamento(s)': clean_marriage(casamento_completo),
            'Morte': cells[4].get_text(strip=True),
            'Ref': cells[5].get_text(strip=True)
        }

        monarchs.append(monarch)

for monarch in monarchs:
    print(monarch)


