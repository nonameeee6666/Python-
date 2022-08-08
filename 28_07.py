from re import X
import pandas as pd  #--> tratamento de base de dados
import matplotlib.pyplot as plt#--> gráficos; quando se põe um ponto após a lib é pq está importando só uma parte dela
import seaborn as sns#--> gráficos, por ter sido feito pelo plt, tem que sempre importar o outro pra usar o seaborn
#junto ao plotly são as bibliotecas mais famosas de criação de gráficos 
from sklearn.model_selection import train_test_split #--> inteligência artificial, é o scikit-learn 
from sklearn.linear_model import LinearRegression #importa um tipo de AI
from sklearn.ensemble import RandomForestRegressor #importa outro tipo de AI
from sklearn.metrics import r2_score #importa o r2

tabela = pd.read_csv("advertising.csv")

print(tabela.corr()) #--> pandas calcula a correlação da tabela

#criação de gráfico da tabela com correlação
sns.heatmap(tabela.corr(), cmap="Purples", annot=True) #heatmap é só um tipo de gráfico, cmap é a cor do gráfico e annot ele irá indicar os valores
#pode ver mais modelos de gráficos e cmap no site do seaborn
plt.show()

#Início do aprendizado de máquina
#criação do y e x, y será quem deseja-se prever e o x quem será o comparativo
#São apenas variáveis, não precisa ser x e y 
x =  tabela[["TV", "Radio", "Jornal"]]
y = tabela["Vendas"]

#pra machine learning é bom dividir o mesmo dado em dados de treino e dados de teste
#isso é útil para analisar se a IA aprendeu, verificando se os dados de teste batem com os dados
#da base, como se "escondesse" da ia alguns dados para analisar se ela está funcionando

#será divido em dados x de treino, x de teste, y de treino e y de teste

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3) #criação das 4 vars
#test_size é pra dizer que 30% será teste e 70% treino
#geralmente usado 20% ou 30%
#a ordem das variáveis devem ser as de cima, o nome tanto faz, mas cada lugar é reservado

#Criação da AI 
#os 2 modelos de AI q serão usados:
regrelinear = LinearRegression() #irá distribuir os valores de treino e traçar uma linha no centro de tudo
arvoredecisi = RandomForestRegressor() #irá decidir e dividir os valores em categorias para chegar em um resultado

#Treino da AI
regrelinear.fit(x_treino, y_treino)
arvoredecisi.fit(x_treino, y_treino)

previ_regrelinear = regrelinear.predict(x_teste)
previ_arvoredecisi = arvoredecisi.predict(x_teste)

#o r2 diz o modelo que melhor consegue explicar em %, pois às vezes podem ter resultados bem semelhantes
print(r2_score(y_teste, previ_regrelinear)) #vai comparar a respota(y_teste) com a previsão
print(r2_score(y_teste, previ_arvoredecisi)) #faz o mesmo só que com a previsão do outro modelo

#criação de gráfico para melhor análise
grafico = pd.DataFrame() #cria uma tabela vazia
grafico["y_teste"] = y_teste #1° coluna com a resposta
grafico["arvore decisao"] = previ_arvoredecisi #2° coluna com o valor da árvore de decisão
grafico["regressao linear"] = previ_regrelinear #3° coluna com o valor da regressão linear

sns.lineplot(data=grafico) #seaborn cria gráfico de linha
plt.show() #matplot exibe

#pode alterar o tamanho do gráfico antes de exibir com: plt.figure(figsize=(15,6))
#o seaborn tbm só pode exibir um gráfico por vez, diferente do plotly

#para fazer mais previsões só precisa de mais dados
#ainda pode fazer mais de uma sessão de análise com IA e criar uma previsão das previsões com AI

#se não quiser em % mas em números é só colocar print direto da var da AI
novos = pd.read_csv("novos.csv")
print(novos)
print(arvoredecisi.predict(novos))
#mas nesse caso o novos.csv já tem os inputs prontos