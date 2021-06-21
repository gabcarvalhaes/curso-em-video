# Programa com função ficha() que recebe dois parâmetros opcionais: nome do jogador e quantos gols ele marcou
# Programa deve mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente
def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gols(s).')


nome = str(input('Digite o nome do jogador: '))
gols =  str(input(f'Quantos gols {nome} fez?'))
if gols.isnumeric():
    gols = int(gols)
else:
    g = 0
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)