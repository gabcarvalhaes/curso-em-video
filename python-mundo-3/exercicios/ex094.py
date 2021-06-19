#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista
#No final, mostre: A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média
dicionario = dict()
lista = list()
tot_pessoas = media_idades = soma_idades = tot_mulheres = pessoas_acima_media = 0
while True:
    nome = str(input('Nome: '))
    sexo = str(input('Sexo: [M/F] ')).upper()
    while sexo not in 'MmFf':
        print('ERRO! Por favor, digite apenas M ou F.')
        sexo = str(input('Sexo: [M/F] ')).upper()
        if sexo in 'MmFf':
            break
    idade = int(input('Idade: '))
    resp = str(input('Quer continuar? [S/N] ')).upper()
    while resp not in 'SsNn':
        print('ERRO! Por favor, digite apenas S ou N.')
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp in 'SsNn':
            break
    dicionario['nome'] = nome
    dicionario['sexo'] = sexo
    dicionario['idade'] = idade
    lista.append(dicionario.copy())
    dicionario.clear()
    tot_pessoas += 1
    soma_idades += idade
    if resp in 'Nn':
        break
media_idades = soma_idades / tot_pessoas
print('-=' * 30)
print(lista)
print(f'A) Ao todo, temos {tot_pessoas} pessoas cadastradas.')
print(f'B) A média de idade é de {media_idades:.2f} anos.')
print(f'C.1) As mulheres cadastradas foram: ')
for k, v in enumerate(lista):
    if lista[k]['sexo'] == 'F':
        tot_mulheres += 1
        print(f'   > {lista[k]["nome"]} ')
print(f'C.2) O total de mulheres cadastradas foi {tot_mulheres}.')
print('D) Lista de pessoas com idade acima da média: ')
for k, v in enumerate(lista):
    if lista[k]['idade'] > media_idades:
        pessoas_acima_media += 1
        print(f'   nome: {lista[k]["nome"]}; sexo: {lista[k]["sexo"]}; idade: {lista[k]["idade"]}')
print('<<ENCERRADO>>')

# Solução do professor Guanabara:

galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'S':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.') #Esqueci que podia usar o len()
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] >= média:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('<<<ENCERRADO>>>')
