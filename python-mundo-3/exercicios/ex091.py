#Programa onde 4 jogadores joguem um dado de 4 lados
#Com resultados aleatórios
#Guarde os resultados num dicionário
#Coloque esse dicionário em ordem crescente
#Sabendo que o vencedor tirou o maior número no dado
from random import randint
from time import sleep
dicionario = {
    'jogador1': randint(1, 4),
    'jogador2': randint(1, 4),
    'jogador3': randint(1, 4),
    'jogador4': randint(1, 4)
}
for k, v in dicionario.items():
    print(f'{k} tirou o valor {v} no dado.')
    print('-=-' * 15)
    sleep(0.5)
print(' ======^ -RANKING DAS MAIORES JOGADAS- ^======')
for v in sorted(dicionario.values(), reverse=True): #Até aqui, consegui colocar a ordem do ranking correto com base no valor das jogadas
    print(v) #Não consegui ir além, infelizmente...

#Solução do professor Guanabara:

from operator import itemgetter
jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
ranking = []
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou o valor {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('=-=' * 30)
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}.')
