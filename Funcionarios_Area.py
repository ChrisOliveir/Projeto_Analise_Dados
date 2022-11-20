import pandas as pd 
import matplotlib
funcionarios = pd.read_csv('CadastroFuncionarios.csv', sep=";", decimal=",")
clientes = pd.read_csv("CadastroClientes.csv", sep=";", decimal=",")
Base = pd.read_excel("BaseServiçosPrestados (1).xlsx", engine='openpyxl')

funcionarios_area = funcionarios['Area'].value_counts()
print(funcionarios_area)
print(funcionarios_area.plot(kind='bar'))