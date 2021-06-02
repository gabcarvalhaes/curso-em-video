# Leia o ano de nascimento de um jovem e informe, de acordo com a idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo de alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano_nasc = int(input('Em que ano nasceu: '))
idade = 2021 - ano_nasc
if idade < 18 and idade != 17 :
    print("""Ainda vai se alistar ao serviço militar.
Faltam {} anos para o alistamento.
""".format(18 - idade))
elif idade == 17 or idade == 18 :
    print('É a hora de se alistar.')
else:
    print('Já passou do tempo de alistamento há {} anos.'.format(idade - 18))

# Solução do professor Guanabara:

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
