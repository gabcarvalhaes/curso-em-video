#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Digite um número: '))
soma = 0
for c in range(1, n + 1):
    if n % c != 0:
        print('\033[31m {}'.format(c), end=' ')
    elif n % c == 0:
        print('\033[33m {}'.format(c), end=' ')
        soma += 1
if soma > 2:
    print('\n\033[97m{} \033[31mNÃO É\033[m um número primo porque é divisível por {} números que o antecedem!'.format(n, soma - 1))
else:
    print('\n\033[97m{} \033[33mÉ\033[m um número primo, pois só é divisível por 1 e por ele mesmo.'.format(n))

#Solução do professor Guanabara:

núm = int(input('Digite um número: '))
tot = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{} '.format(c, end=' '))
print('\n\033[mO número {} foi divisível {} vezes'.format(núm, tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')

