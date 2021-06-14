# Crie um programa que vai ler vários números e colocar em uma lista.
#Mostre quantos números foram digitados
#A lista em ordem decrescente
#Se o valor 5 foi digitado ou não
lista = []
continuar = 'S'
quant_valores = 0
while continuar != 'N':
    lista.append(int(input('Digite um valor: ')))
    quant_valores += 1 #Desnecessário
    continuar = str(input('Deseja continuar? [S/N]')).upper()
    if continuar == 'N':
        break
print(f'Foram digitados {quant_valores} valores.') #Era só mostrar o len(valores), aff...
print(sorted(lista, reverse = True))
print('O valor 5 existe nessa lista!' if 5 in lista else 'O valor 5 não foi digitado.')

#Solução do professor Guanabara:
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'Você digitou {len(valores)} elementos ')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')



