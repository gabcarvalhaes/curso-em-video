palavra = str(input('\033[45;97m Digite uma palavra: \033[m')).upper()
contador = 0
while contador < len(palavra) :
    if palavra[contador] != 'A' :
        print('\033[33m {} \033[m'.format(palavra[contador]))
    contador = contador + 1

