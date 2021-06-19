#Função maior() que leia vários parâmetros e determine o maior valor
from time import sleep


def maior1(*numeros):
    print('Analisando os valores passados...')
    sleep(1)
    cont = 0
    for i in range(0, len(numeros)):
        cont += 1
    print(f'Ao todo, foram digitados {cont} números.')
    print(f'O maior número digitado foi {max(numeros)} .')


maior1(1, 2, 3, 4, 50, 6, 7, 8, 9, 15, 46)

# Outra solução sem utilizar a função max para a tupla gerada
# Utiliza uma variável para armazenar o maior valor analisado

def maior2(*numero):
    cont = maior = 0
    for i in range(0, len(numero)):
        cont += 1
        if numero[i] > maior:
            maior = numero[i]
    print(f'Ao todo, foram digitados {cont} números.')
    print(f'O maior número digitado foi {maior} .')


maior2(1, 2, 5, 2, 3, 7, 14, 32, 222)