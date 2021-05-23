#Antecessor e sucessor de um número:

a = int(input('Digite um número: '))
antecessor = a - 1
sucessor = a + 1
print('O antecessor de {} é igual a {} e o sucessor é igual a {} .'.format(a, antecessor, sucessor))

#Ou podemos utilizar o .format() para realizar as operações para determinar o antecessor e o sucessor:

print('O antecessor de {} é igual a {} e o sucessor é igual a {} .'.format(a, a - 1, a + 1))


