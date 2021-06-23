# Programa com função notas()
# Pode receber várias notas de alunos e vai retornar um dicionário
# Com quantidade de notas, a maior e a menor nota, a média da turma e (opcional) situação
def notas(*n, sit=False):
    """
    Função que gera um boletim em forma de dicionário com base nas notas fornecidas como parâmetro
    :param n: notas a serem lidas
    :param sit: opcional para mostrar a situação do aluno (aprovado, recuperação ou reprovado)
    :return: vai retornar um boletim com a quantidade de notas, maior e menor notas, média e situação (opcional)
    """
    total = media = soma = 0
    boletim = dict()
    for i in range(0, len(n)):
        total += 1
    for i in n:
        soma += i
    media = soma / total
    maior = max(n) #Não faço a menor ideia do porquê eu não atribui direto nos dicionários...
    menor = min(n)
    boletim['total'] = total
    boletim['maior nota'] = maior #Burrice, meu Deus...
    boletim['menor nota'] = menor
    boletim['média'] = media
    if sit:
        if media >= 7:
            boletim['situação'] = 'APROVADO'
        elif 6 <= media <= 7:
            boletim['situação'] = 'RECUPERAÇÃO'
        else:
            boletim['situação'] = 'REPROVADO'
    return boletim


print(notas(8, 6, 7))
help(notas)
