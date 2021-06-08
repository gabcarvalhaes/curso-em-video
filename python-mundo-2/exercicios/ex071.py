#Crie um programa que simule o funcionamento de um caixa eletrônico.
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS:
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('=' * 30)
print('B A N C O  D O  G A B R I E L')
print('=' * 30)
quant_50 = resto_50 = 0
valor_sacar = int(input('Que valor você quer sacar? R$'))
total = valor_sacar
céd = 50
totcéd = 0
while True:
    if total >= céd: #Verificar se da pra tirar R$50 do valor
        total -= céd #Tira R$50 do total
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd == 10
        elif céd == 10:
            céd == 1
        totcéd = 0
        if total == 0:
            break