#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
maior = 0
menor = 0
for i in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(i)))
    if date.today().year - nasc >= 18:
        maior += 1
    else:
        menor += 1
print('''Ao todo tivemos {} pessoas maiores de idade.
E também tivemos {} pessoas menores de idade.'''.format(maior, menor))