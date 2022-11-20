import pandas as pd 

funcionarios = pd.read_csv('CadastroFuncionarios.csv', sep=";", decimal=",")
clientes = pd.read_csv("CadastroClientes.csv", sep=";", decimal=",")
Base = pd.read_excel("BaseServiçosPrestados (1).xlsx", engine='openpyxl')

qts_func_fechou_contrato = len(Base['ID Funcionário'].unique())
qtd_func_total = len(funcionarios['ID Funcionário'])
print(qts_func_fechou_contrato/qtd_func_total)