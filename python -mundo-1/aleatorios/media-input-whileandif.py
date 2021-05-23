contador = int
nome = str(input('Qual o nome do aluno? '))
controle = int(input('Quantas notas deseja registrar para {}?'.format(nome)))
contador = int
soma = float
media = float

contador = 1
soma = 0

while contador <= controle:
 nota = float(input('Digite a nota {}'.format(contador)))
 soma = soma + nota
 contador = contador + 1

media = soma / controle
print('A média de {} é igual a {}'.format(nome, media))

if media >= 7:
    print('Aluno aprovado.')
elif 6 < media < 7:
    print('Aluno em recuperação.')
else:
    print('Aluno reprovado.')