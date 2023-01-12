#Aula 2 
#Projetos de python e automação RPA

#bibliotecas utilizadas 
import pandas as pd
import plotly.express as px


#dataframe do projeto
df = pd.read_csv(r"C:\Users\isauq\Downloads\intensivão pytohn\Aula 2\telecom_users.csv")


df = df.drop("Unnamed: 0", axis=1) # axis -> 0 = linha; axis -> 1= coluna

df["TotalGasto"] = pd.to_numeric(df["TotalGasto"], errors="coerce") #coerce -> força o campo a virar do tipo numérico, caso tenha letras o campo vira null
df= df.dropna(how="all", axis=1)
df= df.dropna(how="any", axis=0)
# print(df["Churn"].value_counts())
# print(df["Churn"].value_counts(normalize=True))
coluna = "TipoContrato"


for coluna in df.columns:
#criação do gráfico
    grafico = px.histogram(df, x=coluna, color="Churn", text_auto=True)
    grafico.show()