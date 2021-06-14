# Programa que o usuário digite uma expressão qualquer que use ()
# Verificar se a abertura e fechamento (a quantidade) de parênteses está correta
expressao = list()
expressao.append(str(input('Digite a expressão: ')))
if expressao[0].count("(") == expressao[0].count(")"):
    print('Expressão VÁLIDA!')
else:
    print('Expressão INVÁLIDA!')

#Solução do professor Guanabara:

expr = str(input('Digite a expressão: '))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')