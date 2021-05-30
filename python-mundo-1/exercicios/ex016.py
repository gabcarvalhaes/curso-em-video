#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math #Importar uma biblioteca traz mais funcionalidades para o seu programa.
número = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(número, math.trunc(número))) #Trunc só retorna a parte inteira do número.

#Poderíamos também só importar uma função específica da biblioteca math
#Dessa forma, ficaria: from math import trunc

from math import trunc
print('O valor digitado foi {} e sua porção inteira é {}'.format(número, trunc(número)))

#Para solucionar esse exercício, há uma maneira que não precisa de importação de biblioteca:

print('O valor digitado foi {} e sua porção inteira é {}'.format(número, int(número))) #Função int já retorna a parte inteira.


