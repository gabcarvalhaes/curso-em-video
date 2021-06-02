# Programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento.
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5%
# em até 2x no cartão: preço normal
# 3x ou mais: 20% de juros

valor = float(input('Digite o valor a ser pago: R$'))
print("""Escolha a forma de pagamento:
1 - À vista dinheiro/cheque
2 - À vista no cartão
3 - 2x no cartão
4 - 3x ou mais parcelas""")
forma = int(input())
if forma == 1 :
    print('O valor do produto, à vista no dinheiro ou cheque, ficará em R${}'.format(valor - (10 * valor) / 100))
elif forma == 2 :
    print('O valor do produto, à vista no cartão, ficará em R${}'.format(valor - (5 * valor) / 100))
elif forma == 3 :
    print('Parcelando em duas vezes, o valor ficará em R${} com duas parcelas no valor de R${}'.format(valor, valor / 2))
elif forma == 4 :
    parcelas = int(input('Quantas parcelas para o pagamento? '))
    print('O valor parcelado em {}x ficará com o valor de R${} (juros de 20% no valor total) e cada parcela irá custar R${}'.format(parcelas, (valor * 1.20), (valor * 1.20) / parcelas))
else:
    print('Não há essa opção. Tente novamente.')