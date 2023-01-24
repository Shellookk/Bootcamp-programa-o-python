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
navegador = webdriver.Chrome()

# passo 1: pegar a cotação do dolar
navegador.get("https://www.google.com.br/")
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação Dolar")
navegador.find_element(By.XPATH, 'html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacaoDolar = navegador.find_element(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

# passo 2: pegar a cotação do Euro
navegador.get("https://www.google.com.br/")
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação Euro")
navegador.find_element(By.XPATH, 'html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacaoEuro = navegador.find_element(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

# passo 3: pegar a cotação do ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")
cotacaoOuro = navegador.find_element(By.XPATH,'//*[@id="comercial"]').get_attribute('value')
cotacaoOuro = cotacaoOuro.replace(",", ".")
navegador.quit()

#passo 4: importar a base de dados e atualizar a base
tabela = pd.read_excel(r'C:\Users\isauq\Downloads\intensivão pytohn\Aula 3\Produtos.xlsx')


tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacaoDolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacaoEuro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacaoOuro)

#passe 5: Recalcular os preços
tabela["Preço de Compra"] = tabela["Cotação"] * tabela["Preço Original"]
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]
print(tabela)

#passo 6: Exportar a base atualizada
tabela.to_excel("base atualizada.xlsx")
#tabela.to_excel("base atualizada.xlsx", index = False)