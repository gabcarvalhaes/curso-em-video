#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
numero_lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_escolhido = random.choice(numero_lista)
palpite = int(input('Tente adivinhar em que número estou pensando... '))
if palpite == numero_escolhido:
    print('Parabéns! Você acertou!')
else:
    while palpite != numero_escolhido:
        palpite = int(input('Você errou! Tente novamente... '))
        if palpite == numero_escolhido:
            print('Parabéns! Você acertou!')

#Solução do professor Guanabara abaixo. Eu esqueci de mostrar o número de palpites acima... :/

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10 .')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))