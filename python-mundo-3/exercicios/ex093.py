# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou
#Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
info_jogador = dict()
lista_gols = list()
total_gols = 0
info_jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {info_jogador["nome"]} jogou? '))
for i in range(0, partidas):
    gols = int(input(f'   Quantos gols na partida {i}? '))
    total_gols += gols
    lista_gols.append(gols)
info_jogador['gols'] = lista_gols
info_jogador['total'] = total_gols
print('-=-' * 30)
print(info_jogador)
print('-=-' * 30)
for k, v in info_jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-=-' * 30)
print(f'O jogador {info_jogador["nome"]} jogou {partidas} partidas.')
for k, v in enumerate(lista_gols):
    print(f'   > Na partida {k}, fez {v} gols.')
print(f'No total, foram {total_gols} gols.')