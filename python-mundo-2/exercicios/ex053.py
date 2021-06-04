#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
palavra = str(input('Digite uma palavra qualquer: '))
palavra_alterada = palavra.replace(" ","").upper() #Substitui onde há " " por ""
s = 0
print('Essa palavra ao contrário é: ')
for i in range(1, len(palavra_alterada) + 1):
    print('{}'.format(palavra_alterada[len(palavra_alterada) - i]), end='')
    if palavra_alterada[len(palavra_alterada) - i] == palavra_alterada[s]:
        s += 1
if s == len(palavra_alterada):
    print('\nA palavra "{}" é um palíndromo!'.format(palavra))
else:
    print('\nA palavra "{}" não é um palíndromo!'.format(palavra))

# Solução do professor Guanabara abaixo:

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #Separou numa lista
junto = ''.join(palavras) #Juntou todos os elementos dessa lista com um ''. Esse processo eliminou os espaços internos.
inverso = ''
for letra in range(len(junto) - 1, -1, -1): #Começar da última letra, vai até o -1 (até o 0, por causa da estrutura for só ir até o penúltimo) e vai voltando uma letra (-1).
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
