# Faça um programa que jogue jokenpô (pedra - papel - tesoura) com você.
import random
from time import sleep
print("""Escolha uma opção:
1 - Pedra
2 - Papel
3 - Tesoura""")
opcoes = [1,2,3]
escolha = int(input())
escolha_pc = random.choice(opcoes)

print('Computador está escolhendo aleatoriamente...')
sleep(2)

if escolha == 1 and escolha_pc == 2 :
    print('O computador escolheu {} . Você PERDEU!'.format(escolha_pc))
elif escolha == 2 and escolha_pc == 3 :
    print('O computador escolheu {} . Você PERDEU!'.format(escolha_pc))
elif escolha == 3 and escolha_pc == 1 :
    print('O computador escolheu {} . Você PERDEU!'.format(escolha_pc))
elif escolha == escolha_pc :
    print('EMPATE.')
else:
    print('O computador escolheu {} . Você GANHOU!'.format(escolha_pc))





