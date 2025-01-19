# Passo a passo do projeto:
# 1º Importar base de dados;
# 2º Visualizar base de dados (entender a base + identificar problemas);
# 3º Tratar base de dados (corrigir problemas na base);
# 4º Análise inicial: quantos clientes cancelaram e qual o percentual (%) de clientes;
# 5º Análise de causa de cancelamento dos clientes.

# Importação da base de dados;
import pandas as pd

tabela = pd.read_csv("cancelamentos.csv")

# 2º Visualizar base de dados (entender a base + identificar problemas);

