#Aprimore o desafio 93 para que ele funcione com vários jogadores
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
info_jogadores = dict()
lista_jogadores = list()
lista_gols = list()
tot_gols = gols = 0
while True:
    info_jogadores['nome'] = str(input('Nome: '))
    info_jogadores['partidas'] = int(input(f'Quantas partidas o jogador {info_jogadores["nome"]} jogou? '))
    for i in range(0, info_jogadores['partidas']):
        gols = int(input(f'Quantos gols foram feitos na partida {i + 1}? '))
        lista_gols.append(gols)
        tot_gols += gols
    info_jogadores['gols'] = lista_gols[:]
    info_jogadores['total'] = tot_gols
    tot_gols = 0
    lista_gols.clear()
    lista_jogadores.append(info_jogadores.copy())
    info_jogadores.clear()
    resp = str(input('Quer continuar? [S/N]')).upper()[0]
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"cod":<4}|{"Nome":>5}{"Gols":>10}{"Total":>12} ')
print('-' * 40)
for k, v in enumerate(lista_jogadores):
    print(f'{str(k):<4}{str(lista_jogadores[k]["nome"]):<10}{str(lista_jogadores[k]["gols"]):>10}{str(lista_jogadores[k]["total"]):>8}')
print('-=' * 30)
option = int
while option != 999:
    option = int(input('Mostrar dados de qual jogador? ("999" encerra) '))
    if option == 999:
        break
    print(f'---LEVANTAMENTO DO JOGADOR: {lista_jogadores[option]["nome"]}')
    print('-' * 30)
    for i, g in enumerate(lista_jogadores[option]['gols']):
        print(f'Na partida {i + 1}, fez {g} gols.')







