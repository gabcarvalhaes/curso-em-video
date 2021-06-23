#Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
from time import sleep
import urllib.request
import webbrowser
try:
    urllib.request.urlopen("http://www.pudim.com.br")
except Exception as erro:  # Desligando o wifi, ou o site não estiver no ar
    print('\033[1; 31mO site Pudim não está acessível no momento.\033[m')
    er = erro  # Variável usada para não ter marcações de erro no código pelo PyCharm.
else:  # Com wifi ligado:
    print('\033[1;32mConsegui acessar o site Pudim com sucesso!\033[m')
    print('Abrindo o site em 3, 2, 1...')
    sleep(3)
    webbrowser.open('http://www.pudim.com.br', new=2)

#Solução do professor Guanabara:
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')