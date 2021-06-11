#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
tupla = ('APRENDER','PROGRAMAR',
         'LINGUAGEM','PYTHON',
         'CURSO','GRATIS',
         'ESTUDAR','PRATICAR',
         'TRABALHAR','MERCADO',
         'PROGRAMAR','FUTURO')
for p in tupla:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end='')

