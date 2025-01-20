# Passo a passo do projeto:
# 1º Importar base de dados;
# 2º Visualizar base de dados (entender a base + identificar problemas);
# 3º Tratar base de dados (corrigir problemas na base);
# 4º Análise inicial: quantos clientes cancelaram e qual o percentual (%) de clientes;
# 5º Análise de causa de cancelamento dos clientes.

# Importação da base de dados;
import pandas as pd
import plotly.express as px

tabela = pd.read_csv("cancelamentos.csv")

# 2º Visualizar base de dados (entender a base + identificar problemas);
print(tabela)

#3º Tratar base de dados (corrigir problemas na base);
tabela = tabela.drop(columns="CustomerID")
print(tabela)

print(tabela.info())

tabela = tabela.dropna()
print(tabela.info())

# 4º Análise inicial: quantos clientes cancelaram e qual o percentual (%) de clientes;
print(tabela["cancelou"].value_counts())

print(tabela["cancelou"].value_counts(normalize=True))

# 5º Análise de causa de cancelamento dos clientes.
for coluna in tabela.columns:

    grafico = px.histogram(tabela, x=coluna, color="cancelou", text_auto=True)

    grafico.show()

