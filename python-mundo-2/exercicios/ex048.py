#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
for n in range(0, 501):
    if n % 3 == 0:
        soma += n
print('A soma entre os múltiplos de 3 é {}'.format(soma))