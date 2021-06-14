#Programa que leia o nome e peso de várias pessoas
#Mostre quantas pessoas foram cadastradas
#Listagem com as pessoas mais pesadas
#Listagem com as pessoas mais leves
primeira_lista = []
peso_pessoas = []
menor = maior = quant_cadastros = 0
mais_pesada = []
menos_pesada = []
resp = 'S'
while True:
    primeira_lista.append(str(input('Nome: ')))
    primeira_lista.append(float(input('Peso: ')))
    quant_cadastros += 1
    peso_pessoas.append(primeira_lista[:])
    primeira_lista.clear()
    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp == 'N':
        break
for i, [nome, peso] in enumerate(peso_pessoas):
    if i == 0:
        maior = menor = peso
    elif peso >= maior:
        maior = peso
    elif peso <= menor:
        menor = peso
for nome, peso in peso_pessoas:
    if peso == maior:
        mais_pesada.append(nome)
    if peso == menor:
        menos_pesada.append(nome)
print(peso_pessoas)
print(f'A quantidade de cadastros realizados foi {quant_cadastros} .')
print(f'O maior peso foi de {maior}Kg. Peso de: ', end='')
for pessoa in mais_pesada:
    print(f'[{pessoa}]', end=' ')
print(f'O menor peso foi de {menor}Kg. Peso de: ', end='')
for pessoa in menos_pesada:
    print(f'[{pessoa}]', end=' ')