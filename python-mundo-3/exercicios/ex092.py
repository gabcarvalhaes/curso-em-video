# Programa que leia nome, ano de nascimento e carteira de trabalho
# Se a carteira de trab for diferente de zero:
# O dicionpario receberá o ano de contratação e o salário
# Mostre a idade e quando a pessoa irá se aposentar
nome = str(input('Nome: '))
data_nascimento = int(input('Data de nascimento: '))
carteira = int(input('Carteira de Trabalho (0 não tem): '))
if carteira == 0:
    dicionario_info = {
        'nome': nome,
        'idade': 2021 - data_nascimento,
        'cttps': 0
    }
    print('-=-' * 30)
    for k, v in dicionario_info.items():
        print(f'- {k} tem o valor {v} .')
else:
    contratacao = int(input('Ano de contratação: '))
    salario = int(input('Salário: R$'))
    aposentadoria = (contratacao - data_nascimento) + 35
    dicionario_info = {
        'nome': nome,
        'idade': 2021 - data_nascimento,
        'cttps': carteira,
        'contratacao': contratacao,
        'salario': salario,
        'aposentadoria': aposentadoria
    }
    print('-=-' * 30)
    for k, v in dicionario_info.items():
        print(f'- {k} tem o valor {v} .')

#Solução do professor Guanabara:
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=-' * 30)
for k, v in dados.items():
    print(f'{k} tem valor {v}')