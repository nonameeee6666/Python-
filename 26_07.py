import pandas as pd
import plotly.express as px

tabela = pd.read_csv(r"C:\Users\nonam\Downloads\telecom_users.csv")
tabela = tabela.dropna(how="all", axis=1)
tabela = tabela.dropna(how="any", axis=0)
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
#print(tabela.info())
#print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))
#print(tabela["Churn"].value_counts())
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)
    grafico.show()
