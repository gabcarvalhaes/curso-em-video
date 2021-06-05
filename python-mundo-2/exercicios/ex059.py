# Menu de opções com: somar, multiplicar, maior, novos números e sair do programa. Com dois valores input.
primeiro_valor = int(input('Digite o primeiro valor: '))
segundo_valor = int(input('Digite o segundo valor: '))
opção = int
# 1- soma / 2- mult / 3- maior / 4-novos números / 5- sair
while opção != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opção = int(input('>>>>Qual é a sua opção? '))
    if opção == 1:
        print('A soma entre {} e {} é {}'.format(primeiro_valor, segundo_valor, primeiro_valor + segundo_valor))
    elif opção == 2:
        print('O resultado da multiplicação desses valores é {}'.format(primeiro_valor * segundo_valor))
    elif opção == 3:
        if primeiro_valor > segundo_valor:
            print('O maior valor entre {} e {} é {}'.format(primeiro_valor, segundo_valor, primeiro_valor))
        else:
            print('O maior valor entre {} e {} é {}'.format(primeiro_valor, segundo_valor, segundo_valor))
    elif opção == 4:
        primeiro_valor = int(input('Digite um novo valor: '))
        segundo_valor = int(input('Digite outro novo valor: '))
    else:
        print('Programa finalizado.')

