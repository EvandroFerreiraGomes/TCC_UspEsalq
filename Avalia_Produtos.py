# Este script detecta produtos com chocolate com base em palavras-chave
# Autor: Evandro Gomes Ferreira - TCC do MBA em Data Science da USP Esalq

import pandas as pd

# Caminhos
CAMINHO_BASE = r"D:\TCC_BASES\Produtos.csv"
CAMINHO_SAIDA = r"D:\TCC_BASES\Produtos_com_chocolate.csv"

# Lista de palavras-chave (você pode expandir)
palavras_chave = [
    'choco', 'chocolate', 'cobertura', 'brigadeiro', 'brownie', 'trufa',
    'trufado', 'cappuccino', 'nescau', 'toddy', 'nutella', 'ganache',
    'chocotone', 'bombom', 'alpino', 'prestígio', 'alfajor', 'mousse de chocolate'
]

# Função para checar se há alguma palavra-chave no nome do produto
def verifica_chocolate(texto):
    texto = str(texto).lower()
    return int(any(palavra in texto for palavra in palavras_chave))

# Leitura da base com separador correto
df = pd.read_csv(CAMINHO_BASE, sep=';', encoding='utf-8-sig')
df.columns = df.columns.str.strip().str.lower()
df.dropna(subset=['produto'], inplace=True)

# Aplicação da função
df['usa_chocolate'] = df['produto'].apply(verifica_chocolate)

# Salvar resultado
df.to_csv(CAMINHO_SAIDA, sep=';', index=False, encoding='utf-8-sig')
print("Arquivo salvo com sucesso em:", CAMINHO_SAIDA)