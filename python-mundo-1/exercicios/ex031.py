#Programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.

distancia = float(input('Distância da viagem:'))
passagem = float
if distancia <= 200:
    passagem = distancia * 0.50
    print('O preço da passagem ficou em R${} .'.format(passagem))
else:
    passagem = distancia * 0.45
    print('O preço da passagem ficou em R${} .'.format(passagem))
