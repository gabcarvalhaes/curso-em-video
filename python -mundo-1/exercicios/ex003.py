#Soma entre dois números

n1 = input('Digite um valor: ')
n2 = input('Digite outro valor: ')
soma = n1 + n2
print('A soma entre {} e {} é igual a {}'.format(n1, n2, soma)) #A soma mostrará a combinação entre os dois valores digitados pois não houve declaração de tipos primitivos de dados.

#Solução correta:

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
print('A soma entre {} e {} é igual a {} '.format(n1, n2, soma))

#Ou utilizando o próprio .format() para realizar a operação (sem precisar utilizar a variável 'soma'):

print('A soma entre {} e {} é igual a {} '.format(n1, n2, (n1+n2)))


