# Passo 1: Importar a base de dados
import pandas as pd

tabela = pd.read_csv("telecom_users.csv")

# Passo 2: Visualizar a base de dados
tabela = tabela.drop("Unnamed: 0", axis=1)
display(tabela)
# - Entender quais as informações tão disponíveis

# Passo 3: Tratamento de dados
# - Valores que estão reconhecidos de forma errada
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# - Valores vazios
# deletando as colunas vazias
# axis = 0 _> linha ou axis = 1 _> coluna
tabela = tabela.dropna(how="all", axis=1)
# deletando as linhas vazias
tabela = tabela.dropna(how="any", axis=0)

print(tabela.info())

# Passo 4: Análise Inicial
# Como estão os nossos cancelamentos?
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

# Passo 5: Análise Mais completa
# comparar cada coluna da minha tabela com a coluna de cancelamento
import plotly.express as px

# etapa 1: criar o gráfico
for coluna in tabela.columns:
    # para edições nos gráficos: https://plotly.com/python/histograms/
    # para mudar a cor do gráfico , color_discrete_sequence=["blue", "green"]
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)
    # etapa 2: exibir o gráfico
    grafico.show()

# Conclusões:

# Clientes com contrato mensal tem MUITO mais chance de cancelar:

# Podemos fazer promoções para o cliente ir para o contrato anual
# Familias maiores tendem a cancelar menos do que famílias menores

# Podemos fazer promoções pra pessoa pegar uma linha adicional de telefone
# MesesComoCliente baixos tem MUITO cancelamento. Clientes com pouco tempo como cliente tendem a cancelar muito

# A primeira experiência do cliente na operadora pode ser ruim
# Talvez a captação de clientes tá trazendo clientes desqualificados
# Ideia: a gente pode criar incentivo pro cara ficar mais tempo como cliente
# QUanto mais serviços o cara tem, menos chance dele cancelar

# podemos fazer promoções com mais serviços pro cliente
# Tem alguma coisa no nosso serviço de Fibra que tá fazendo os clientes cancelarem

# Agir sobre a fibra
# Clientes no boleto tem MUITO mais chance de cancelar, então temos que fazer alguma ação para eles irem para as outras formas de pagamento