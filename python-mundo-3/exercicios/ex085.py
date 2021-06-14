#Programa que o usuário digite sete valores numéricos e cadastre-os numa lista
#Dentro dessa lista, os valores pares tem que ficar separados dos ímpares
#No final, mostre os valores pares e ímpares em ordem crescente
lista_num = [[], []]
for i in range(0, 7):
    num = int(input('Digite um número inteiro qualquer: '))
    if num % 2 == 0:
        lista_num[0].append(num)
    else:
        lista_num[1].append(num)
lista_num[0].sort()
lista_num[1].sort()
print(f'Os números pares digitados foram {lista_num[0]}')
print(f'Os números ímpares digitados foram {lista_num[1]}')

