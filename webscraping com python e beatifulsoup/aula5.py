import requests
from bs4 import BeautifulSoup
import re

url = 'https://pt.wikipedia.org/wiki/Lista_de_monarcas_da_Inglaterra'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')
tables = soup.find_all('table', class_='wikitable')

# A tabela de Wessex é a terceira (índice 2)
t2 = tables[2]
rows = t2.find_all('tr')

monarchs = []

def clean_name(name):
    # Remove referências [12] e números
    return re.split(r'\[|\d', name)[0].strip()

def clean_birthdate(birthdate):
    match = re.match(r'^\d+(?:/\d+)?', birthdate)
    return match.group() if match else birthdate

def clean_marriage(marriage):
    cleaned = re.sub(r'\d+', '', marriage)
    cleaned = re.sub(r'\bfilhos?\b', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned

def clean_death(death):
    # Procura o padrão: dia + mês + ano (de 3 ou 4 dígitos)
    # O \b garante que o ano não esteja grudado na idade
    match = re.search(
        r'(\d{1,2} de [a-zç]+ de )(\d{3,4})\b',
        death,
        re.IGNORECASE
    )

    if match:
        return match.group(1) + match.group(2)

    # Caso não ache a frase completa, tenta pegar apenas o ano isolado
    match = re.search(r'\b\d{3,4}\b', death)
    if match:
        return match.group()

    return death

# Loop principal
for row in rows[1:]:
    cells = row.find_all(['th', 'td'])

    if len(cells) == 6:
        # O SEGREDO: Adicionamos um espaço " " como separador ao extrair o texto
        # Isso evita que o HTML <a>939</a><span>43 anos</span> vire 93943
        nome_completo = cells[0].get_text(" ", strip=True)
        nascimento_completo = cells[2].get_text(" ", strip=True)
        casamento_completo = cells[3].get_text(" ", strip=True)
        morte_completo = cells[4].get_text(" ", strip=True)

        img = cells[1].find('img')
        image_url = "https:" + img['src'] if img else "N/A"

        monarch = {
            'Nome': clean_name(nome_completo),
            'Retrato': image_url,
            'Nascimento': clean_birthdate(nascimento_completo),
            'Casamento(s)': clean_marriage(casamento_completo),
            'Morte': clean_death(morte_completo),
            'Ref': cells[5].get_text(strip=True)
        }
        monarchs.append(monarch)

# Exibição dos resultados
for monarch in monarchs:
    print(monarch)




import pandas as pd
df = pd.DataFrame(monarchs)
df.to_csv('monarcas_wessex.csv', index=False, encoding='utf-8-sig')
