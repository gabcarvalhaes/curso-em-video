#rie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = list()
n = int(input('Digite um valor inteiro: '))
lista.append(n)
option = 'S'
while option == 'S':
    option = str(input('Você quer continuar? [S/N]')).upper()
    if option.upper() == 'S':
        n = int(input('Digite um valor inteiro: '))
        if n not in lista:
            lista.append(n)
        else:
            print('Valor duplicado! Não é possível adicioná-lo.')
    else:
        print('Programa finalizado.')
        print(sorted(lista))

#Solução do professor Guanabara:

números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
números.sort()
print(f'Você digitou os valores {números}')

