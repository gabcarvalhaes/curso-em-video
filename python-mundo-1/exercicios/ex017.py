#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2) #Método puramente matemático no python.
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

#Podemos importar a biblioteca math e tornar isso mais simples:

import math

hipotenusa = math.hypot(cateto_oposto, cateto_adjacente) #Os catetos são parâmetros dessa função hypot.
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
