# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(p)))
    if p == 1: #Se for a primeira ocorrência do laço.
        maior = peso #Isso é necessário porque, senão, mais tarde, o menor e o maior vão ficar com o mesmo valor.
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {}kg'.format(maior))
print('O menor peso foi {}kg'.format(menor))








