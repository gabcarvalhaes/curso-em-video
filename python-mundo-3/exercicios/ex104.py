# Programa que tenha a função leiaInt()
# Fazendo validação para aceitar apenas valor numérico
def leiaInt(string):
    string = str(input('Digite um número: '))
    while string.isnumeric() == False:
        print('\033[31mERRO!Digite apenas um número inteiro!\033[m')
        string = str(input('Digite um número: '))
    if string.isnumeric():
        return int(string)


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n} .')