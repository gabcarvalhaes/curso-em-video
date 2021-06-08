#Crie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuário vai continuar ou não.
#No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
decisão = 'S'
soma_preços = produtos_acima_mil = menor = cont = 0
mais_barato = str
while decisão in 'S':
    print('-' * 20)
    print('SUPERMERCADO')
    print('-' * 20)
    nome_produto = str(input('Produto: ')).strip().upper()
    preço_produto = float(input('Preço:R$'))
    soma_preços += preço_produto
    cont += 1
    if preço_produto > 1000:
        produtos_acima_mil += 1
    if cont == 1:
        menor = preço_produto
    else:
        if preço_produto < menor:
            menor = preço_produto
            mais_barato = nome_produto
    decisão = str(input('Quer registrar mais algum produto? [S/N] ')).strip().upper()
    if decisão in 'N':
        print('FIM DOS REGISTROS.')
        print(f'No total, você gastou R${soma_preços}')
        print(f'Você comprou {produtos_acima_mil} produtos acima de R$1000 .')
        print(f'O produto mais barato foi {mais_barato} .')