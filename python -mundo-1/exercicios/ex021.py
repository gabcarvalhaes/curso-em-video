# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame  # Para implementar uma das soluções desse exercício, precisamos importar a biblioteca pygame.

pygame.init()  # Inicia o uso da biblioteca.
pygame.mixer.music.load('ex021.mp3')  # Carregar o arquivo .mp3 previamente salvo na pasta dos arquivos python.
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass #Na época que o professor Guanabara gravou a resolução desse exercício, o pygame era um pouco diferente. Hoje, o código usado para dar o play nesse áudio é esse.

#Outra solução mais simples (dentre várias outras):

from playsound import playsound
playsound('ex021.mp3')
