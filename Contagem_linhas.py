# Esse código varre todos os arquivos CSV que começam com "estabelecimentos"
# dentro de uma pasta específica, conta o número de linhas (exceto cabeçalhos)
# em cada um deles e exibe o total consolidado. Útil para auditoria de bases grandes.
# Autor: Evandro Gomes Ferreira
# Conteúdo do TCC do MBA em Data Science da USP Esalq

import pandas as pd
import glob
import os

pasta = r'D:/TCC_BASES/'
arquivos = glob.glob(os.path.join(pasta, 'estabelecimentos*.csv'))
total_linhas = 0

for arquivo in arquivos:
    linhas = sum(1 for _ in open(arquivo, encoding='latin1')) - 1  # -1 para subtrair o cabeçalho
    print(f'{os.path.basename(arquivo)}: {linhas} linhas')
    total_linhas += linhas

print(f'\nTotal de linhas (sem contar cabeçalhos): {total_linhas}')