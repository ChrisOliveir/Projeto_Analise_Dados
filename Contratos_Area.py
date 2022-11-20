import pandas as pd 

funcionarios = pd.read_csv('CadastroFuncionarios.csv', sep=";", decimal=",")
clientes = pd.read_csv("CadastroClientes.csv", sep=";", decimal=",")
Base = pd.read_excel("BaseServiçosPrestados (1).xlsx", engine='openpyxl')

print(funcionarios)
print(Base)

contratos_area = Base[['ID Funcionário']].merge(funcionarios[['ID Funcionário', 'Area']], on="ID Funcionário") #dentro do merge fica a tabela que vai dar informações
print(contratos_area)
