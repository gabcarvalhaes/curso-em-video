#Mostrar o dobro, o triplo e a raíz quadrada de um número:

a = int(input('Digite um número: '))
dobro = a * 2
triplo = a * 3
raiz = a ** (1/2) #Um número elevado a 1/2 é equivalente a sua raíz quadrada.
print('O dobro de {} é igual a {} . '.format(a, dobro))
print('O triplo de {} é igual a {} .'.format(a, triplo))
print('A raíz quadrada de {} é igual a {} . '.format(a, raiz))

#Podemos reunir todas as informações numa só linha:

print('O dobro de {} vale {}, o triplo vale {} e a raíz quadrada vale {} .'.format(a, dobro, triplo, raiz))

#Podemos limitar o número de casas decimais dentro de um valor a ser exibido num {} :

print('A raíz quadrada de {} é igual a {:.2f}'.format(a, raiz)) #Aqui, o '2f' equivale a duas casas decimais flutuantes (do tipo float).


