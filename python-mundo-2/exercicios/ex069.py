#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
print('-' * 20)
print('CADASTRE UMA PESSOA')
print('-' * 20)
resp = 'S'
quant_pessoas_18 = homem = mulheres_menos_20 = 0
while resp in 'Ss':
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    print('-' * 20)
    if idade > 18 or sexo == 'M':
        quant_pessoas_18 += 1
        homem += 1
    elif sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        print(f'Temos {quant_pessoas_18} pessoas com mais de 18 anos.')
        print(f'Também temos {homem} homens cadastrados.')
        print(f'Além disso, temos {mulheres_menos_20} mulheres com menos de 20 anos.')

