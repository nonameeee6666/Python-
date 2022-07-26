from turtle import delay, left, right
from numpy import quantile
import openpyxl
import pyautogui
import time
import pandas
import pyperclip

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
pyautogui.write(quantidade)
#pyautogui.hotkey("ctrl", "enter")