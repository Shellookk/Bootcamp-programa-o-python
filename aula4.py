#importação de bibliotecas
import pandas as pd
import matplotlib as plt
import seaborn as sns

tabela = pd.read_csv(r"C:\Users\isauq\Downloads\intensivão pytohn\Aula 4\advertising.csv")


#cria o grafico
sns.heatmap(tabela.corr())

#exibe o gráfico