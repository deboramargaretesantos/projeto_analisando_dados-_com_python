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

# Análise dos gráficos e ações para resolução das possíveis causas de cancelamento do serviço:

# Causa: Usuários de contrato mensal sempre cancelam.
# Ação corretiva: evitar o contrato mensal e incentivar (com desconto) os contratos trimestrais e anuais.

# Causa: Todos os usuários que ligam mais de 4x para o call center, cancelaram o serviço.
# Ação: Criar um alerta vermelho, que acuse quando o usuário já realizou a terceira ligação para o call center.

# Causa: Usuários que atrasaram o pagamento por mais de 20 dias, cancelaram o serviço.
# Ação: Criar alerta para quando o usuário atingiu 15 dias de atraso no pagamento.

# Com essas três ações estratégicas é possível reduzir consideravelmente o percentual de cancelamento:
