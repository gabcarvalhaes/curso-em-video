#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
#5 primeiros times
#4 últimos colocados
#Ordem alfábetica
#Posição da Chapecoense
brasileirão = ('Fortaleza', 'Athletico - PR', 'Atlético - GO', 'Bragantino', 'Bahia', 'Fluminense', 'Palmeiras', 'Flamengo',
                'Atlético - M', 'Corinthians',
                'Ceará', 'Santos', 'Cuiabá', 'Sport', 'São Paulo',
                'Juventude', 'Internacional',
                'Grêmio', 'América - MG', 'Chapecoense')
print(f'Os 5 primeiros times são: {brasileirão[:6]}')
print(f'Os 4 últimos colocados são: {brasileirão[16:21]}')
print(sorted(brasileirão))
print(f'A Chapecoense ocupa a posição {brasileirão.index("Chapecoense") + 1}')