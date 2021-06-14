#Crie uma matriz 3x3
#Mostre a soma dos valores pares
#Mostre a soma dos valores da terceira coluna
#Mostre o maior valor da segunda linha
matriz = [0, 0, 0], [0, 0, 0], [0, 0, 0]
soma_pares = maior = soma_terceira_coluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor [{l}][{c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        if matriz[l][c] == matriz[l][2]:
            soma_terceira_coluna += matriz[l][2]
        if matriz[l][c] == matriz[1][c]:
            if matriz[1][c] > maior:
                maior = matriz[1][c]
print(f'A soma dos valores pares é {soma_pares} .')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna} .')
print(f'O maior valor da segunda linha é {maior}')