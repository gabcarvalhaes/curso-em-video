# Programa que faça o computador pensar num número aleatório e 0 a 5 e peça para o usuário tentar adivinhar qual foi. Se acertar, mostrará alguma mensagem, senão, mostrará outra mensagem.

import random
numero_lista = [0, 1, 2, 3, 4, 5]
numero_escolhido = random.choice(numero_lista)
palpite = int(input('Qual foi o número escolhido entre 0 e 5? '))

if palpite == numero_escolhido:
    print('Você acertou! Parabéns!')
else:
    print('Você errou!')

#Solução do professor Guanabara abaixo:

from random import randint
from time import sleep #biblioteca pra tempo
computador = randint(0, 5) #Faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3) #Esperar 3 segundos
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}'.format(computador, jogador))