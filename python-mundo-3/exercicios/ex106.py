# Mini sistema que utilize o interactive help do Python
# O usuário vai digitar o comando e o manual vai aparecer
# Quando digitar "fim", o programa se encerrará
c = ('\033[m',
     '\033[0;107;41m'
     )

def ajuda(com):
    help(com)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)
    print(c[0], end='')

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)