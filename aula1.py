#bibliotecas
import pyautogui as py
import pyperclip as pyp
import time
import pandas as pd
py.press("Win")
py.write("google chrome")
py.press("Enter")
time.sleep(1)
py.click(x=949, y=609, clicks=2)
time.sleep(1)
py.hotkey("ctrl", "t")
pyp.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
py.hotkey("ctrl","v")
py.press("enter")
time.sleep(3)
py.click(x=476, y=376, clicks=2)
time.sleep(2)
py.click(x=476, y=376, clicks=1)
time.sleep(2)
py.click(x=1669, y=247)
time.sleep(2)
py.click(x=1453, y=743)
time.sleep(5)

tb = pd.read_excel(r"C:\Users\isauq\Downloads\Vendas - Dez.xlsx")
print(tb)
faturamento = tb["Valor Final"].sum()
quantidade = tb["Quantidade"].sum()

py.hotkey("ctrl", "t")
pyp.copy("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
py.hotkey("ctrl","v")
py.press("enter")
time.sleep(2)
py.click(x=85, y=260)
time.sleep(1)
py.write("isauqejk123@gmail.com")
time.sleep(1)
py.press("tab")
time.sleep(1)
py.press("tab")
time.sleep(1)
pyp.copy("Relatório de vendas")
time.sleep(1)
py.hotkey("ctrl", "v")
py.press("tab")
text = """Prezado Paulo,
esse email é um teste do treinamento da #treinamento
O faturamento foi de R$: {faturamento:,.2f}
E a quantidade de produtos foi de: {quantidade:,.2f}
att. Isaque Rodrigues
"""
pyp.copy(text)
py.hotkey("ctrl", "v")
py.hotkey("ctrl", "enter")


# time.sleep(5)
# print(py.position())
