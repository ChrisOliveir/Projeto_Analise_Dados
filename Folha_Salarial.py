import pandas as pd 

funcionarios = pd.read_csv('CadastroFuncionarios.csv', sep=";", decimal=",")
#clientes = pd.read_csv("CadastroClientes.csv")
#Base = pd.read_excel("BaseServiçosPrestados.xlsx")


# RETIRANDO COLUNAS ESTADO CIVIL E CARGO 

funcionarios = funcionarios.drop(['Estado Civil', 'Cargo'], axis=1)


funcionarios['Salario Total'] =  funcionarios['Salario Base'] + funcionarios['Impostos'] + funcionarios['Beneficios'] + funcionarios['VT'] + funcionarios['VR']
print('Total da folha salarial mensal é de R${:,}'.format(funcionarios['Salario Total'].sum()))