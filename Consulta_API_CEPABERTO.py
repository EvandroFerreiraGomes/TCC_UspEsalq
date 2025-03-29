# Esse código realiza consultas na API do CEP Aberto para obter dados completos
# a partir de uma lista de CEPs em um arquivo Excel. Garante a preservação dos
# zeros à esquerda, mantendo o CEP no formato correto e salvando os dados em CSV.
# Autor: Evandro Gomes Ferreira
# Conteúdo do TCC do MBA em Data Science da USP Esalq

import pandas as pd
import requests
import time

arquivo = r'D:\TCC_BASES\Base_CEP.xlsx'
planilha = 'CEP'
saida_csv = r'D:\TCC_BASES\CEP_Geocodificado.csv'

# crie um conta no CepAberto.com e acesse https://www.cepaberto.com/api_key
token = "...."
headers = {'Authorization': f'Token token={token}'}

df_ceps = pd.read_excel(arquivo, sheet_name=planilha)
df_ceps['CEP'] = (
    df_ceps['CEP']
    .astype(str)
    .str.replace(r'\D', '', regex=True)
    .str.zfill(8)
)
ceps_validos = df_ceps['CEP'].dropna().drop_duplicates().tolist()

dados = []

for cep in ceps_validos:
    url = f"https://www.cepaberto.com/api/v3/cep?cep={cep}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200 and response.json():
        data = response.json()
        data['cep'] = cep
        dados.append(data)
    else:
        print(f'CEP inválido ou sem dados: {cep}')
    time.sleep(1)

if dados:
    df_resultado = pd.json_normalize(dados)
    df_resultado.to_csv(saida_csv, index=False)
    print(f'Concluído, salvo como {saida_csv}')
else:
    print('Erro')