#Aula 3 do intensivão de python Hashtag da programação

#Bibliotecas
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

# rodar o navegador
# para rodar o chrome em 2º plano
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.headless = True 
# navegador = webdriver.Chrome(options=chrome_options)
# navegador = webdriver.Chrome()

# passo 1: pegar a cotação do dolar
# navegador.get("https://www.google.com.br/")
# navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação Dolar")
# navegador.find_element(By.XPATH, 'html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
# cotacaoDolar = navegador.find_element(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
# print(cotacaoDolar)

# passo 2: pegar a cotação do Euro
# navegador.get("https://www.google.com.br/")
# navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação Euro")
# navegador.find_element(By.XPATH, 'html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
# cotacaoEuro = navegador.find_element(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
# print(cotacaoEuro)

# passo 3: pegar a cotação do ouro
# navegador.get("https://www.melhorcambio.com/ouro-hoje")
# cotacaoOuro = navegador.find_element(By.XPATH,'//*[@id="comercial"]').get_attribute('value')
# print(cotacaoOuro)

#passo 4: importar a base de dados e atualizar a base
tabela = pd.read_excel(r'C:\Users\isauq\Downloads\intensivão pytohn\Aula 3\Produtos.xlsx')
print(tabela)
#passe 5: Recalcular os preços

#passo 6: Exportar a base atualizada

 