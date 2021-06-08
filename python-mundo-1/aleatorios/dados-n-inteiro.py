n = int(input('Digite um número: '))
contador = int
resultado = int
a = int
s = int
fibonacci1 = int
fibonacci2 = int
nextfibonacci = int
controle = int
position = int

a = n - 1
s = n + 1

print('Tabuada do {}:'.format(n))

contador = 1
resultado = n * contador

while contador <= 10:
    print('{} x {} = {}'.format(n, contador, resultado))
    contador = contador + 1

if n%2 == 0:
    print('{} é um número par.'.format(n))
else:
    print('{} é um número ímpar.'.format(n))

print('Seu antecessor é {} e seu sucessor é {} .'.format(a, s))

fibonacci1 = 0
fibonacci2 = 1
position = 0

for controle in range(0, 10000):
    nextfibonacci = fibonacci1 + fibonacci2
    fibonacci2 = fibonacci1
    fibonacci1 = nextfibonacci
    position = position + 1

    if nextfibonacci == n:
        true_position = position
        print('A posição do número {} na Sequência de Fibonacci é {} .'.format(n, true_position))
        break
    elif nextfibonacci > n:
        print('Esse número não existe na Sequência de Fibonacci.')
        break



