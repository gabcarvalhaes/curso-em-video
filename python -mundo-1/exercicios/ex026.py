#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite qualquer coisa: ')).upper().strip()
print('Quantas vezes a letra "A" aparece: ', frase.count('A'))
print('Posição que aparece a letra "A" pela primeira vez: ', frase.find('A'))
print('Posição que aparece a letra "A" pela última vez: ', frase.rfind('A')) #.rfind() para começar a procurar a partir da direita.
