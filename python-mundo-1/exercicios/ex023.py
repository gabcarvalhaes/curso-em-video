#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
number = str(input('Digite um número de 0 a 9999: '))
print("""
dezena: {}
centena: {}
milhar: {}
""".format(number[3], number[2], number[1], number[0]))

#O código acima só irá funcionar para números com 4 dígitos. Se tiver menos, dará erro.
#O código abaixo irá funcionar para todos os casos e utiliza uma solução puramente matemática através do módulo da divisão:

number = int(input('Digite um número: '))
unidade = number // 1 % 10
dezena = number // 10 % 10
centena = number // 100 % 10
milhar = number // 1000 % 10
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
