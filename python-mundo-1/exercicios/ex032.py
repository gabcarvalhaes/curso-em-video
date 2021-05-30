#Programa que leia um ano qualquer e mostre se é bissexto ou não.
ano = int(input('Digite um ano: '))
if ano % 4 == 0:
    if ano % 100 != 0:
        print('Esse ano é bissexto!')
    elif ano % 100 == 0:
        if ano % 400 == 0:
            print('Esse ano é bissexto!')
        else:
            print('Não é bissexto.')
else:
    print('Não é bissexto.')

#Solução do professor Guanabara abaixo:

from datetime import date
ano = int(input('Que ano quer analisa Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} não é BISSEXTO!'.format(ano))
