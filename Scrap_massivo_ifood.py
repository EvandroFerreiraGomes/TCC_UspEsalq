# Esse código automatiza a navegação por uma lista de links do iFood armazenados em um arquivo .txt,
# captura o conteúdo visível da página com CTRL+A e CTRL+C e salva em arquivos sequenciais .txt
# o objetivo é realizar o scraping massivo e posteriormente o tratamento através de outro algoritmo
# Autor: Evandro Gomes Ferreira
# Conteúdo do TCC do MBA em Data Science da USP Esalq

import time
import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# CONFIG CAMINHOS
arquivo_links = r'D:\TCC_BASES\Links_Ifood.txt'
pasta_saida = r'D:\TCC_BASES\SCRAP'

with open(arquivo_links, 'r', encoding='utf-8') as f:
    links = [linha.strip() for linha in f if linha.strip()]

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

for i, url in enumerate(links, start=1):
    try:
        print(f'Link {i}/{len(links)}: {url}')
        driver.get(url)
        time.sleep(6)  # Aguarda carregar

        pyautogui.click(x=500, y=300)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)

        conteudo = pyperclip.paste()
        nome_arquivo = f'{pasta_saida}\\link{i}.txt'
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            f.write(conteudo)

        print(f'Salvo em: {nome_arquivo}')
        time.sleep(1.5)

    except Exception as e:
        print(f'Erro {i}: {e}')
        continue

driver.quit()
print('\n Finalizado')