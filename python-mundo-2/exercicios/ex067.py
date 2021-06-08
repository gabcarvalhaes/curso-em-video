#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.
m = n = 1
while n > 0:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        print('Finalizado.')
        break
    m = 1
    while m <= 10:
        print(f'{m} x {n} = {m * n}')
        m += 1

#Solução do professor Guanabara:
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 30)
print('Programa tabuada encerrado.')