# Este código automatiza a navegação por links do iFood, clica no botão "Ver mais",
# copia o conteúdo visível da página e salva em arquivos .txt
# Autor: Evandro Gomes Ferreira
# Conteúdo do TCC do MBA em Data Science da USP Esalq

import time
import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        time.sleep(3)  # tempo para carregar os elementos iniciais da página

        try:
            botao_ver_mais = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Ver mais')]"))
            )
            botao_ver_mais.click()
            print("Botão 'Ver mais' clicado.")
            time.sleep(1)
        except:
            print("Botão 'Ver mais' não encontrado ou já visível.")

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
print('\nFinalizado')
