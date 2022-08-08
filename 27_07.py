import pandas as pd
import datetime
from selenium import webdriver #importa o webdriver para abrir o navegador
from selenium.webdriver.common.keys import Keys #importa as teclas

driver_path = "C:/Users/nonam\AppData/Local/Microsoft/WindowsApps/chromedriver.exe" #path do driver
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe" #path do navegador

option = webdriver.ChromeOptions() 
option.binary_location = brave_path

# Create new Instance of Chrome
navegador = webdriver.Chrome(executable_path=driver_path, chrome_options=option) 
#até aq era só pra funcionar no brave

#Cotação dólar
navegador.get("https://www.google.com.br/") #inicia o navegador no google

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotacao dolar") #escreve no xpath do campo de pesquisa
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER) #aperta enter no xpath do campo de pesquisa
cotacao_dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value") #pega o value do xpath
#.click() para clicar em um xpath
print(cotacao_dolar)

#Cotação euro
navegador.get("https://www.google.com.br/") #inicia o navegador no google

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotacao euro") #escreve no xpath do campo de pesquisa
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER) #aperta enter no xpath do campo de pesquisa
cotacao_euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value") #pega o value do xpath
#.click() para clicar em um xpath
print(cotacao_euro)

#Cotação ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje") #inicia o navegador no google

cotacao_ouro = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute("value") #pega o value do xpath
#.click() para clicar em um xpath
cotacao_ouro = cotacao_ouro.replace(",", ".") #muda uma info por outra, no caso a vírgula por ponto
print(cotacao_ouro)

navegador.quit() #fecha o navegador

#atualização da tabela

tabela = pd.read_excel("Produtos.xlsx") #localiza o arquivo a ser analisado

tabela.loc[tabela["Moeda"]=="Dólar" , "Cotação"] = float(cotacao_dolar) #localiza dentro da tabela alguma info
#a área onde tem a tabela é a área de coluna, no caso a coluna é uma condição  de onde a moeda for igual a Dólar
#poderia ser substituído por um if

#agr mesmo pro ouro e euro
tabela.loc[tabela["Moeda"]=="Euro" , "Cotação"] = float(cotacao_euro) #atualiza as cotações
tabela.loc[tabela["Moeda"]=="Ouro" , "Cotação"] = float(cotacao_ouro) #também já transforma em float

tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"] #atualiza o preço de acordo com a cotação
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"] #atualiza o preço de venda

print(tabela)

data = datetime.datetime.now() #guarda a data atual
data = data.strftime("%Y-%m-%d") #formatação da data atual só pro ano, mês e dia
tabela.to_excel("Produtos "+data+".xlsx", index=False) #exporta a tabela pra uma tabela com a data atual