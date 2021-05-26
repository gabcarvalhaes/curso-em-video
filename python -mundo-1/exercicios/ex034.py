#Programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00 o aumento é de 10%.
#Para os inferiores ou iguais, é de 15%.
salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + ( salário * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salário, novo))
