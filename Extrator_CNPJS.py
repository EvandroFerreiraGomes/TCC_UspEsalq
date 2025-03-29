import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from datetime import datetime
import os

def encontrar_url_mais_recente(base_url):
    hoje = datetime.today()
    for _ in range(2):  # tenta o mes atual, se não tiver, o anterior
        ano_mes = hoje.strftime('%Y-%m')
        url = f"{base_url}{ano_mes}/"
        print(f"Tentando acessar: {url}")
        response = requests.get(url)
        if response.status_code == 200:
            print(f"URL encontrada: {url}")
            return url, response.text
        # volta um mês
        if hoje.month == 1:
            hoje = hoje.replace(year=hoje.year - 1, month=12)
        else:
            hoje = hoje.replace(month=hoje.month - 1)
    raise Exception("Link incorreto")

def baixar_arquivos_da_pagina(html, url_base, pasta_destino):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')
    arquivos = [link.get('href') for link in links if link.get('href') and link.get('href').endswith('.zip')]

    os.makedirs(pasta_destino, exist_ok=True)

    for nome_arquivo in arquivos:
        url_arquivo = url_base + nome_arquivo
        caminho_destino = os.path.join(pasta_destino, nome_arquivo)

        print(f"Baixando: {nome_arquivo}")
        response = requests.get(url_arquivo, stream=True)
        tamanho_total = int(response.headers.get('content-length', 0))

        with open(caminho_destino, 'wb') as f, tqdm(
            desc=nome_arquivo,
            total=tamanho_total,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                bar.update(len(chunk))

# CONFIGURACAO
base_url = "https://arquivos.receitafederal.gov.br/dados/cnpj/dados_abertos_cnpj/"
destino = r"D:\TCC_BASES"

# EXECUCAO
url_final, html = encontrar_url_mais_recente(base_url)
baixar_arquivos_da_pagina(html, url_final, destino)
