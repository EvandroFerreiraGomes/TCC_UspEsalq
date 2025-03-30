# Coleta de links da página do iFood usando Selenium com WebDriver Manager
# Autor: Evandro Gomes Ferreira — TCC MBA em Data Science USP Esalq

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
#options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--log-level=3')

# Corrigido: uso explícito do Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.ifood.com.br/restaurantes/"
driver.get(url)
time.sleep(10)

# Scroll para carregar mais estabelecimentos
for _ in range(15):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# Coleta os links
links = driver.find_elements(By.TAG_NAME, "a")
urls = [link.get_attribute('href') for link in links if link.get_attribute('href') and '/delivery/' in link.get_attribute('href')]
urls = list(set(urls))

# Mostra os links na tela
print(f"\n{len(urls)} links encontrados:\n")
for url in urls:
    print(url)

# Salva os links em um arquivo
with open("urls_ifood.txt", "w", encoding="utf-8") as f:
    for url in urls:
        f.write(url + "\n")

driver.quit()