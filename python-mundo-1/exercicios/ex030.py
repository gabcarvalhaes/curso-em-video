#Programa que leia um número inteiro e mostra na tela se é PAR ou impar

number = int(input('Digite um número: '))
if number % 2 == 0:
    print('É par.')
else:
    print('É ímpar.')