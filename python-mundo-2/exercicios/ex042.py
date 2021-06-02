# Refaça o desafio 35 acrescentando o tipo de triângulo que será formado:
# Equilátero: todos os lados iguais;
# Isósceles: dois lados iguais;
# Escaleno: todos os lados diferentes.
print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: #Condição para formação de um triângulo
    print('Os segmentos acima PODEM FORMAR um triângulo!')
    if r1 == r2 and r2 == r3 :
        print('É um triângulo EQUILÁTERO.')
    elif r1 == r2 or r1 == r3 :
        print('É um triângulo ISÓSCELES.')
    else:
        print('É um triângulo ESCALENO.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')

