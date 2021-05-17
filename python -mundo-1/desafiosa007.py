n = int(input('Digite um número: '))
t = int
print('Seu sucessor é {} e seu antecessor é {}'.format(n+1, n-1))
print('O seu dobro é {}, o seu triplo é {} e sua raíz quadrada é {}'.format(n*2, n*3, n**1/2))

t = 1
while (t <= 10):
    print('{} x {} = {}'.format(n, t, n*t))
    t = t + 1

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

print('A média entre {} e {} é igual a {}'.format(n1, n2, (n1+n2)/2))


