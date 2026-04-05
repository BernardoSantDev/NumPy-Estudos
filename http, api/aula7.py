#Salvando Dados de API em CSV, Excel e Outros Formatos

#
#
#
#
#
#
#
#Salvando em CSV (DataFrame.to_csv)
#Exemplo básico
import pandas as pd

dados = [
    {"id_venda": 1, "produto": "Teclado",     "categoria": "Periféricos", "preco": 200.0, "quantidade": 1, "cidade": "Juiz de Fora"},
    {"id_venda": 2, "produto": "Mouse",       "categoria": "Periféricos", "preco": 150.0, "quantidade": 2, "cidade": "São Paulo"},
    {"id_venda": 3, "produto": "Monitor 24\"", "categoria": "Monitores",  "preco": 900.0, "quantidade": 1, "cidade": "Rio de Janeiro"},
    {"id_venda": 4, "produto": "Cadeira Gamer","categoria": "Móveis",     "preco": 1200.0,"quantidade": 1, "cidade": "Juiz de Fora"},
    {"id_venda": 5, "produto": "Headset",     "categoria": "Periféricos", "preco": 300.0, "quantidade": 1, "cidade": "São Paulo"},
    {"id_venda": 6, "produto": "Mouse",       "categoria": "Periféricos", "preco": 150.0, "quantidade": 3, "cidade": "Rio de Janeiro"}
]

df = pd.DataFrame(dados)
df["valor_total"] = df["preco"] * df["quantidade"]
df.to_csv("vendas.csv")


#Opções importantes do to_csv
#index
#Geralmente, quando vamos compartilhar o CSV com outras pessoas/sistemas, é melhor usar index=False para evitar confusão.
df.to_csv("vendas_sem_indice.csv", index=False)

#sep – separador
#Isso é útil quando:
#O sistema de destino espera ; como separador.
#Os dados possuem muitas vírgulas, e você quer evitar problemas.
df.to_csv("vendas_ponto_virgula.csv", sep=";", index=False)

#encoding – codificação
#Se seus dados têm acentos (muito comum em português), é importante pensar em encoding.
#encoding="utf-8" é o padrão em muitos casos (e é o recomendado).
#Em alguns sistemas mais antigos/Windows, às vezes usam latin1 ou iso-8859-1.
df.to_csv("vendas_utf8.csv", index=False, encoding="utf-8")







#Carregando um CSV de volta com pandas
#Criar/limpar/transformar DataFrame.
#Salvar em CSV.
#Mais tarde (ou em outro notebook/script), carregar esse CSV.
## Salvando
df.to_csv("vendas.csv", index=False)

# Carregando depois...
df_novo = pd.read_csv("vendas.csv")

print(df_novo.head())
print(df_novo.info())

#Se você usou sep=";" ao salvar, precisa usar o mesmo ao ler:
df_novo = pd.read_csv("vendas_ponto_virgula.csv", sep=";")







#Salvando em Excel (to_excel)
#Requisitos
#Para salvar em .xlsx, é comum precisar de um engine, como openpyxl. Se der erro, você pode instalar:
#pip install openpyxl
#Exemplo básico
df.to_excel("vendas.xlsx")


#Opções importantes do to_excel
#index=False para não salvar o índice:
df.to_excel("vendas_sem_indice.xlsx", index=False)
#sheet_name para escolher o nome da aba:
df.to_excel("relatorio_vendas.xlsx", index=False, sheet_name="Vendas 2025")





#Salvando em JSON (to_json)
#Às vezes queremos manter o formato mais próximo da API, mas com dados já tratados.
#Formato padrão (registros em colunas)
#O pandas vai salvar com uma estrutura onde cada coluna vira uma chave, e os índices viram sub-chaves. Nem sempre é o mais intuitivo pra reuso em outras aplicações.
df.to_json("vendas.json")

#Formato “records” (lista de objetos)
#Para manter o formato parecido com uma lista de dicionários (como veio da API), use:
df.to_json("vendas_records.json", orient="records", force_ascii=False)
#orient="records" → salva como lista de objetos:
#force_ascii=False → permite salvar acentos corretamente.

#Carregando JSON de volta
#Se você salvou com orient="records", pode ler assim:
df_json = pd.read_json("vendas_records.json", orient="records")
print(df_json.head())





#Exemplo completo: salvando versões “bruta” e “limpa”
import pandas as pd

# Simulando dados brutos de uma API
dados_brutos = [
    {"id": 1, "cliente": " Ana ", "valor": "250.0", "cidade": "juiz de fora"},
    {"id": 2, "cliente": "Bruno", "valor": "300",   "cidade": "SÃO PAULO"},
    {"id": 3, "cliente": "Carla", "valor": None,    "cidade": "Rio de Janeiro"}
]

df_bruto = pd.DataFrame(dados_brutos)

# 1) Salvar dados brutos em CSV
df_bruto.to_csv("data/raw/vendas_bruto.csv", index=False)

# 2) Fazer limpeza simples
df_limpo = df_bruto.copy()
df_limpo["cliente"] = df_limpo["cliente"].str.strip()
df_limpo["cidade"] = df_limpo["cidade"].str.title()
df_limpo["valor"] = pd.to_numeric(df_limpo["valor"], errors="coerce")

# Preencher valores faltantes de valor com 0 (exemplo)
df_limpo["valor"] = df_limpo["valor"].fillna(0)

# 3) Salvar dados limpos em CSV e Excel
df_limpo.to_csv("data/processed/vendas_limpo.csv", index=False, encoding="utf-8")
df_limpo.to_excel("data/processed/vendas_limpo.xlsx", index=False)

# 4) Salvar também em JSON no formato records
df_limpo.to_json("data/processed/vendas_limpo.json", orient="records", force_ascii=False)






