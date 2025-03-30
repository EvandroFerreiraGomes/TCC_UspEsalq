# Esse código realiza a extração automatizada de dados de arquivos .txt copiados do iFood,
# identificando informações relevantes como nome do estabelecimento, pedido mínimo, nota,
# endereço, cidade, CEP e CNPJ. Ele percorre todos os arquivos da pasta indicada, trata
# quebras de linha e variações no formato dos dados, e organiza o resultado em um arquivo CSV.
# Autor: Evandro Gomes Ferreira
# Conteúdo do TCC do MBA em Data Science da USP Esalq

import os
import re
import pandas as pd

# Config
pasta = r"D:\TCC_BASES\SCRAP\"

dados = []

for nome_arquivo in os.listdir(pasta):
    if nome_arquivo.endswith(".txt"):
        caminho = os.path.join(pasta, nome_arquivo)
        with open(caminho, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.read().splitlines()

            nome = None
            endereco = None
            cidade_uf = None
            pedido_minimo = None
            nota = None
            cep = None
            cnpj = None

            # estabelecimento
            for i, linha in enumerate(linhas):
                if "Ver mais" in linha:
                    for j in range(i - 1, -1, -1):
                        if linhas[j].strip():
                            nome = linhas[j].strip()
                            break
                    break

            # pedido mínimo
            for linha in linhas:
                if "Pedido mínimo R$" in linha:
                    pedido_minimo_match = re.search(r"R\$ ?([\d,.]+)", linha)
                    if pedido_minimo_match:
                        pedido_minimo = pedido_minimo_match.group(1).replace(",", ".")
                    break

            # Nota
            for i, linha in enumerate(linhas):
                if "Buscar no cardápio" in linha:
                    for j in range(i - 1, -1, -1):
                        if linhas[j].strip():
                            nota = linhas[j].strip()
                            break
                    break

            # endereço e cidade
            for i, linha in enumerate(linhas):
                if "Endereço" in linha and i + 6 < len(linhas):
                    endereco = linhas[i + 4].strip()
                    cidade_uf = linhas[i + 5].strip()
                    break

            # CEP
            for linha in linhas:
                cep_match = re.search(r"CEP: ?([\d\-]+)", linha)
                if cep_match:
                    cep = cep_match.group(1)
                    break

            # CNPJ
            for linha in linhas:
                cnpj_match = re.search(r"CNPJ: ?([\d./\-]+)", linha)
                if cnpj_match:
                    cnpj = cnpj_match.group(1)
                    break

            dados.append({
                "Arquivo": nome_arquivo,
                "Estabelecimento": nome,
                "Pedido Mínimo (R$)": pedido_minimo,
                "Nota": nota,
                "Endereço": endereco,
                "Cidade/UF": cidade_uf,
                "CEP": cep,
                "CNPJ": cnpj
            })

df = pd.DataFrame(dados)

df.to_csv(r"D:\TCC_BASES\scrap_ifood.csv", index=False, sep=';', encoding='utf-8-sig')