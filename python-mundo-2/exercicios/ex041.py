# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a sua idade:
# até 9 anos: mirim
# até 14 anos: infantil
# até 19 anos: junior
# até 25 anos: sênior
# acima: master
ano_nasc = int(input('Ano de nascimento do atleta: '))
idade = 2021 - ano_nasc #Estou considerando 2021 como ano atual para a operação
if idade <= 9 :
    print('Atleta MIRIM.')
elif idade <= 14 :
    print('Atleta INFANTIL.')
elif idade <= 19 :
    print('Atleta JUNIOR.')
elif idade <= 25 :
    print('Atleta SÊNIOR.')
else:
    print('Atleta MASTER.')