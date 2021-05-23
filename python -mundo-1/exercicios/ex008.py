#Programa que leia um valor em metros e o exiba convertido em centímetros e milímetros:

medida = float(input('Digite uma distância em metros: '))
cent = medida * 100
mili = medida * 1000
print('A distância em centímetros é {}cm e em milímetros é {}mm'.format(cent, mili))

