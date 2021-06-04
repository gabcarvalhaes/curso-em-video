#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
primeiro_termo = int(input('Digite um número: '))
razao = int(input('Digite a razão dessa progressão aritmética: '))
for i in range(0, 10):
    print(primeiro_termo)
    primeiro_termo += razao

#Solução do professor Guanabara:

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{} '.format(c), end=' ')
print('Acabou.')
