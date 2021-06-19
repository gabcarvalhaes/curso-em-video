# Programa que tenha uma função chamada contador()
# Recebe três parâmetros: início, fim e passo(razão)
# Tem que realizar três contagens através da função criada
# de 1 até 10, de 1 em 1
# de 10 até 0, de 2 em 2
# contagem personalizada
from time import sleep


def contador():
    i = 0
    while i <= 10:
        print(i, end=' ')
        sleep(0.25)
        i += 1
    j = 10
    print('\n-' * 3)
    while j >= 0:
        print(j, end=' ')
        sleep(0.25)
        j -= 2
    print('\n-' * 3)
    print('Personalize sua contagem:')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    if inicio > fim:
        while inicio >= fim:
            print(inicio, end=' ')
            sleep(0.25)
            inicio -= passo
    elif fim > inicio:
        while fim >= inicio:
            print(inicio, end=' ')
            sleep(0.25)
            inicio += passo
    print('\nContagem finalizada!')


contador()
