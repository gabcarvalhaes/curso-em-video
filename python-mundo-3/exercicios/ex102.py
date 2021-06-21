# Programa com função fatorial() que receba dois parâmetros:
# o primeiro indica o número a calcular e outro chamado show
# o show será um valor lógica e opcional
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial
def fatorial(n, show=False):
    f = 1
    for i in range(n, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f
print(fatorial(5, True))