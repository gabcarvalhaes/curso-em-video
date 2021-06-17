# Programa que leia nome e média de um aluno.
# Armazenando tudo isso num dicionário
# Mostre o conteúdo da estrutura da tela
aluno = {}
aluno['nome'] = str(input('Aluno: '))
aluno['média'] = float(input('Média: '))
print('-' * 25)
print(f'Nome do aluno(a): {aluno["nome"]}')
print(f'A média do aluno(a) é {aluno["média"]}')
if aluno['média'] >= 7:
    print('Aluno aprovado.')
elif aluno['média'] >= 6:
    print('Aluno em recuperação.')
else:
    print('Aluno reprovado.')

#Solução do professor Guanabara:

estudante = dict()
estudante['nome'] = str(input('Nome: '))
estudante['média'] = float(input(f'Média de {aluno["nome"]}: '))
 

