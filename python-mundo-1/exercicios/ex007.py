#Calcular a média aritmética de duas notas de um aluno:

nota1 = float(input('Digite a primeira nota: ')) #Variável tipo float pois a nota pode ter casa decimal, não vai ser sempre um valor inteiro.
nota2 = float(input('Digite a segunda nota: '))
média = (nota1 + nota2)/2
print('A média do aluno é {} .'.format(média))
