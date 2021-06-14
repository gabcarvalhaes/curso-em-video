#Programa que ajude um jogador da MEGA SENA a criar palpites.
#Pergunta quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo
#cadastrando tudo em uma lista composta
from time import sleep
from random import randint
print('-' * 20)
print('JOGOS NA MEGA SENA')
print('-' * 20)
jogo = [[], [], [], [], [], []]
quant_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {quant_jogos} JOGOS -=-=-=')
for i in range(0, quant_jogos):
    jogo[i] = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    print(f'Jogo {i+1}: {jogo[i]}')
    print('_' * 35)
    sleep(1)
print('-=-=-=-= < BOA SORTE! > -=-=-=-=')

#Solução do professor Guanabara (sem repetir os números... esqueci dessa condição):

lista = list()
jogos = list()
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont+= 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)