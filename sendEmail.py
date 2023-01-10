# instalar bibliotecas
# !pip install pyautogui
# !pip install pyperclip
# !pip install time

# ferramenta para envio de e-mail referente à faturamento diário 

import pyautogui
import pyperclip
import time 

pyautogui.PAUSE = 1

# Passo 1: Entrar no sistema da empresa (no nosso caso é o link do drive)
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(5)

# Passo 2: Navegar no sistema e encontrar a base de vendas (entrar na pasta exportar)
pyautogui.click(x=2321, y=459, clicks=2)
time.sleep(2)


# Passo 3: Fazer o download da base de vendas
pyautogui.click(x=2317, y=530, clicks=1) # clicar no arquivo
pyautogui.click(x=3144, y=342) # clicar nos 3 pontinhos
pyautogui.click(x=2961, y=767) # clicar no fazer download
time.sleep(5) # esperar o download acabar

# Passo 4: Importar a base de vendas pro Python
import pandas as pd

tabela = pd.read_excel(r"/home/proempresa/Downloads/Vendas - Dez.xlsx")
display(tabela)

# Passo 5: Calcular os indicadores da empresa
faturamento = tabela["Valor Final"].sum()
print(faturamento)
quantidade = tabela["Quantidade"].sum()
print(quantidade)

# Passo 6: Enviar um e-mail para a diretoria com os indicadores de venda

# abrir aba
pyautogui.hotkey("ctrl", "t")

# entrar no link do email - https://mail.google.com/mail/u/0/#inbox
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)

# clicar no botão escrever
pyautogui.click(x=1993, y=348)

# preencher as informações do e-mail
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # selecionar o email

pyautogui.press("tab") # pular para o campo de assunto
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab") # pular para o campo de corpo do email

texto = f"""
Prezados,

Segue relatório de vendas.
Faturamento: R${faturamento:,.2f}
Quantidade de produtos vendidos: {quantidade:,}

Qualquer dúvida estou à disposição.
Att.,
Jv Barros
"""

# formatação dos números (moeda, dinheiro)

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

# enviar o e-mail
pyautogui.hotkey("ctrl", "enter")