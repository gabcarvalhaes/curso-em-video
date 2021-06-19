# Programa que tenha uma lista chamada números e duas funções
# sorteia() e somaPar()
# A função sorteia() vai sortear 5 números e vai colocá-los dentro da lista
# A outra vai mostrar a soma entre todos os valores pares sorteados anteriormente
from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando os 5 valores da lista:')
    for i in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}...', end=' ')
        sleep(0.3)
    print(f'A lista ficou assim: {lista}')




def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'\nA soma entre os valores pares é {soma} .')


numeros = list()
sorteia(numeros)
somaPar(numeros)