#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input('Digite a largura: '))
alt = float(input('Digite a altura: '))
área = larg * alt
print('Sua parede tem a dimensão {}x{} e sua área é de {}m²'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(tinta))
