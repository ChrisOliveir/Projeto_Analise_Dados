# Projeto Analise de Dados

Esse projeto foi inicializado com: [Create React App](https://github.com/facebook/create-react-app).

## Scripts Disponíveis

No diretório do projeto, você pode executar:

### `pip install -r requirements.txt`

Para instalar dependências do projeto, como pacotes já instalados.

## Análise que queremos do Projeto

1 - Valor total da folha salarial, qual foi o gasto total com salarios de funcionarios da empresa?
Sugestão: Calcule o salário total de cada funcionario, salario + beneficios + impostos, depois some todos os salarios.

2 - Qual foi o faturamento da empresa?
Sugestão: Calcule o faturamento total de cada serviço e depois some o faturamento de todos.

3 - Qual o % de funcionarios que ja fechou algum contrato?
Sugestão: na base de serviços temos o funcionarios que fechou cada serviço. Mas nem todos os funcionarios que a empresa tem ja fecharam algum serviço.
Na base de funcionarios temos uma lista com todos os funcionarios.
Qqueremos calcular a qtd_func_fecharam_serviço / qdt_funcionarios_totais
para calcular a qtd de funcionarios que fecharam algum serviço , use a base de serviços e conte quantos funcionarios tem ali. Porem cada funcionario so pode ser contado uma unica vez.

4 -Calcule o total de contratos que cada area da empresa ja fechou

5 - Calcule o total de funcionarios por area.

6 - Qual o ticket médio mensal(faturamento médio mensal dos contratos)?

## Etapas do Projeto 

1 - Importe o Pandas:

    import pandas as pd 

2 - Extrair as bases de dados
    
    pd.read_csv("base") --> para arquivos CSV
    pd.read_excel("base) --> para arquivos XLSX

3 - Retirar colunas da base que nao iremos usar:
   
    df.drop(['Estado Civil', 'Cargo'], axis=1)
