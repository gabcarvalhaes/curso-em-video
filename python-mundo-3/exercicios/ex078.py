#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = []
maior = menor = 0
for i in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
print(f'O maior valor foi {maior} na posições ')
for p, v in enumerate(lista):
    if v == maior:
        print(f'{p}...', end='')
print(f'\nO menor valor foi {menor} nas posições ')
for p, v in enumerate(lista):
    if v == menor:
        print(f'{p}...', end='')