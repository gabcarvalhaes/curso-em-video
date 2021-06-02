# Programa para aprovar o empréstimo bancário de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
valor_casa = float(input('Valor da casa: '))
salario_comprador = float(input('Salário do comprador: '))
anos_pagamento = int(input('Em quantos anos vai pagar tudo: '))
meses_pagamento = anos_pagamento * 12

prestacao_mensal = valor_casa / meses_pagamento

if prestacao_mensal > (30 * salario_comprador) / 100:
    print('Empréstimo bancário negado.')
else:
    print('Empréstimo permitido.')

#Solução do professor Guanabara:
casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='') # end='' para a próxima linha do print vir aqui pro lado desse print.
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO.')
else:
    print('Empréstimo NEGADO.')