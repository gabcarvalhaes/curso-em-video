#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma_idade = 0
media_idade = 0
mais_velho = 0
nome_mais_velho = str
f_menos_vinte = 0
for i in range(1,5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(i)))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(i)))
    soma_idade += idade
    sexo = str(input('Digite o sexo da {}ª pessoa [M/F]: '.format(i))).upper()
    if sexo == 'M' and idade > mais_velho:
        mais_velho = idade
        nome_mais_velho = nome
    if sexo == 'F' and idade < 20:
        f_menos_vinte += 1
media_idade = soma_idade / 4
print('''A média da idade das pessoas é {}
O nome do homem mais velho é {}
E a quantidade de mulheres com menos de vinte anos é {}'''.format(media_idade, nome_mais_velho, f_menos_vinte))
