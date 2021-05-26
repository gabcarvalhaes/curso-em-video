#Programa que leia a velocidade de um carro.
#Se ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por Km ACIMA do limite.

velocidade = float(input('Qual foi a velocidade do carro? (Km/h) '))
multa = 7
pagar = float

if velocidade > 80:
    pagar = (velocidade - 80)*7
    print('Você foi multado.')
    print('Velocidade limite excedida. Sua multa é de R${} .'.format(pagar))
else:
    print('Não foi multado.')