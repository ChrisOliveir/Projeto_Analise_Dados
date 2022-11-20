import pandas as pd 

funcionarios = pd.read_csv('CadastroFuncionarios.csv', sep=";", decimal=",")
clientes = pd.read_csv("CadastroClientes.csv", sep=";", decimal=",")
Base = pd.read_excel("BaseServiçosPrestados (1).xlsx", engine='openpyxl')

faturamento = Base[['ID Cliente', 'Tempo Total de Contrato (Meses)']].merge(clientes[['ID Cliente', 'Valor Contrato Mensal']], on='ID Cliente')
faturamento['Faturamento Total'] = faturamento['Tempo Total de Contrato (Meses)'] * faturamento['Valor Contrato Mensal']
print('Total do faturamento é de R${:,}'.format(faturamento['Faturamento Total'].sum()))