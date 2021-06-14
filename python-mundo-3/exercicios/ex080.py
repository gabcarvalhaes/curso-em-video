#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
#já na posição correta de inserção (sem usar o sort())
#No final, mostre a lista ordenada na tela.
a = b = 0
list = [4, 6, 1, 2, 0]
while a < 4:
    b = a + 1
    while b < 5:
        if list[a] > list[b]:
            temp = list[b]
            list[b] = list[a]
            list[a] = temp
        b += 1
        a += 1
print(list)

#Não consegui pensar numa solução...
#Solução do professor Guanabara abaixo:
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]: #Lógica de if simplificado com duas condições com or
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print(f'O valores digitados em ordem foram: {lista}')


