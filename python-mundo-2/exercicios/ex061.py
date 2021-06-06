#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão dessa PA: '))
i = 1
while i <= 10:
    proximo_termo = primeiro_termo + razao
    primeiro_termo += razao
    print('{}'.format(proximo_termo), end='')
    print(' FIM ' if i == 10 else ' -> ', end='')
    i += 1