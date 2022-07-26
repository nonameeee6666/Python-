from turtle import delay, left, right
from numpy import quantile
import openpyxl
import pyautogui
import time
import pandas
import pyperclip
pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")
#pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=2300, y=250, clicks=2)
time.sleep(1.5)
pyautogui.click(x=2300, y=350)
pyautogui.click(x=2300, y=350, button='right')
pyautogui.click(x=2450, y=820)
time.sleep(5)
pyautogui.press("enter")
time.sleep(7)


tabela = pandas.read_excel(r"C:\Users\nonam\Downloads\Vendas - Dez.xlsx")
quantidade = tabela["Quantidade"].sum()
faturamento = tabela["Valor Final"].sum()

pyautogui.PAUSE = 1
pyautogui.hotkey("ctrl", "t")
pyautogui.write("gmail.com")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=2000, y=150)
time.sleep(2)
pyautogui.write("pedrodiassartorio@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")
pyperclip.copy("Relatório de vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
conteúdo = """Prezados, bom dia

Segue o valor da quantidade e faturamento de produtos

Faturamento: R${faturamento:,.2f}
Quantidade: R${quantidade:,.2f}

"""
pyperclip.copy(conteúdo)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter")