# Esse código descompacta todos os arquivos ZIP do diretório armazenado em "pasta_zip"
# em uma nova pasta chamada "extraidos" dentro do diretório anterior
# Autor: Evandro Gomes Ferreira
# Conteúdo do TCC do MBA em Data Science da USP Esalq

import os
import zipfile

pasta_zip = r'D:\TCC_BASES'
pasta_destino = os.path.join(pasta_zip, 'extraidos')
os.makedirs(pasta_destino, exist_ok=True)

for arquivo in os.listdir(pasta_zip):
    if arquivo.endswith('.zip'):
        caminho_zip = os.path.join(pasta_zip, arquivo)
        try:
            print(f'Extraindo: {arquivo}...')
            with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
                zip_ref.extractall(pasta_destino)
            print(f'Concluído: {arquivo}')
        except Exception as e:
            print(f'Falhou: {arquivo}: {e}')

print('Processo concluído.')
