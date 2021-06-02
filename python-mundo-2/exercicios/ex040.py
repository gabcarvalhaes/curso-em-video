# Leia duas notas de um aluno e calcule sua média, mostrando uma mensagem de acordo com a média:
# < 5 = reprovado
# entre 5 e 6.9 =  recuperação
# 7 ou superior = aprovado

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5 :
    print('A média é {} . O aluno está reprovado.'.format(media))
elif media >= 5 and media <= 6.9 :
    print('A média é {}. O aluno está em recuperação.'.format(media))
else:
    print('A média é {}. Aluno aprovado.'.format(media))