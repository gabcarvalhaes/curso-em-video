# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
#Quantas vezes aparece o 9.
#Em que posição foi digitado o primeiro valor 3.
#Quais foram os números pares.
qntd_pares = 0
valores = tuple(int(input('Digite um número: '))for c in range(0, 4))
print(f'O número 9 aparece {valores.count(9)} vezes.')
if 3 not in valores:
    print('O número 3 não existe nessa tupla.')
else:
    print(f'O primeiro número 3 foi digitado na posição {valores.index(3)}')
print('Os números pares dessa tupla são: ')
for i in valores:
    if i % 2 == 0:
        print(i, end='  ')
        qntd_pares += 1
if qntd_pares == 0:
    print('Nenhum')

#Solução do professor Guanabara:

núm = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print(f'Você digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes.')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3)}ª posição.')
else:
    print('O número 3 não foi digitado em nenhuma posição.')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')




