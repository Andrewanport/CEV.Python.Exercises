# Exercício Python 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
# .

import pygame
pygame.init()
pygame.mixer.music.load('') # Entre as aspas coloque o áudio que tem baixado
pygame.mixer.music.play()
pygame.event.wait()