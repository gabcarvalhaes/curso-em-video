#Crie um programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas.

#– Quantas letras ao todo (sem considerar espaços).

#– Quantas letras tem o primeiro nome.

nome_completo = str(input('Digite um nome completo: '))
print('O nome em maísculas é: ', nome_completo.upper())
print('O nome em minúsculas é:', nome_completo.lower())
print('Quantidade de letras ao todo (sem espaço) é ', len(nome_completo) - nome_completo.count(' ')) #Subtraímos da quantidade de caracteres totais (len()) a quantidade de espaços vazios existentes.
nome_split = nome_completo.split()
print('O primeiro nome possui {} letras'.format(len(nome_split[0])))