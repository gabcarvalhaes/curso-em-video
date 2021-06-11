#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
extensos = ('zero', 'um', 'dois', 'três','quatro', 'cinco', 'seis', 'sete', 'oito','nove','dez', 'onze', 'doze', 'treze', 'quatorze','quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numero = int(input('Digite um numero de 0 a 20: '))
while numero not in range(0,21):
	numero = int(input('Tente novamente.Digite um numero de 0 a 20: '))
print(f'Você digitou o numero {extensos[numero]}!')

#Solução do professor Guanabara:

cont = ('zero', 'um', 'dois', 'três','quatro',
		'cinco', 'seis', 'sete', 'oito','nove',
		'dez', 'onze', 'doze', 'treze', 'quatorze',
		'quinze', 'dezesseis', 'dezessete', 'dezoito',
		'dezenove', 'vinte')
while True:
	núm = int(input('Digite um número entre 0 e 20: '))
	if 0 <= núm <= 20:
		break
	print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[núm]} .')