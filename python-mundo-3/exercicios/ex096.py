# Função que tenha o nome área()
#Receba as dimensões de um terreno retangular como parâmetros (largura x comprimento)
#Mostre a área
def area(l, c):
    a = l * c
    print(f'As dimensões são {l} x {c} e a área é {a} .')

area(int(input('Largura: ')), int(input('Comprimento: ')))