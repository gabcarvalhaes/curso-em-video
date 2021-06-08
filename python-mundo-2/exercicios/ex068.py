#Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
result_soma = str
par_ou_impar = str
vitorias = 0
while True:
    print('=-' * 15)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('=-' * 15)
    n = int(input('Diga um valor: '))
    par_ou_impar = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print('-' * 20)
    computador = randint(0, 10)
    soma = computador + n
    print(f'Você jogou {n} e o computador {computador} . Total de {computador + n} deu ', end='')
    if soma % 2 == 0:
        print('PAR!')
        result_soma = 'P'
    else:
        print('ÍMPAR!')
        result_soma = 'I'
    if result_soma == par_ou_impar:
        print('Você VENCEU! Vamos jogar novamente...')
        vitorias += 1
    else:
        print('Você PERDEU!')
        print(f'Você teve {vitorias} vitórias consecutivas!')
        break

#Solução do professor Guanabara:
#Biblioteca random já importada!
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes consecutivas.')




