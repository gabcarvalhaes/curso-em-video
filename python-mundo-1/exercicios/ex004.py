#Dissecando uma variável:

a = input('Digite algo: ') #A função 'input' sozinha sempre retorna uma string(str).
print('Tipo de dado: ', type(a)) #type() mostra o tipo de dado primitivo

#A função x.is...() testa o tipo de valor que foi inserido. É um número inteiro? É alfanumérico? É alfabético? Segue os exemplos abaixo:

print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfanumérico? ', a.isalnum())
print('É alfabético? ', a.isalpha())
print('Está em maiúsculas?', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())

