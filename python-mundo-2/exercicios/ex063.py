# Gere a Sequência de Fibonacci com 'n' termos que o usuário vai escolher.
n = int(input('Quantos termos você deseja visualizar na Sequência de Fibonacci? '))
i = 1
fibonacci1 = 0
fibonacci2 = 1
while i <= n:
    nextfibonacci = fibonacci1 + fibonacci2
    fibonacci2 = fibonacci1
    fibonacci1 = nextfibonacci
    print('{}'.format(nextfibonacci), end='')
    print(' FIM' if i == n else ' -> ', end='')
    i += 1
