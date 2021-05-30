#Conversor de moedas, considerando o dólar a R$3,27:

real = float(input('Quantos reais você tem? R$'))
dólar = real / 3.27
print('Com R${} , você pode comprar US${:.2f}'.format(real, dólar))
