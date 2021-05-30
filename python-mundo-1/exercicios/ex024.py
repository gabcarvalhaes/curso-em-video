#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cidade = str(input('Digite o nome da cidade: '))
cidade_split = cidade.split()
print('Começa com "Santo"?', 'SANTO' in cidade_split[0].upper())

#Solução que utilizei para esse exercício. Abaixo, podemos observar a solução utilizada pelo Guanabara:

cidade = str(input('Em que cidade você nasceu? ')).strip() #.strip para eliminar espaços logo ao separar.
print(cidade[:5].upper() == 'SANTO') #[:5] do início até o 5 ele transforma tudo em maiúscula com o .upper() e verifica se é igual a SANTO através do ==