import pygame

pygame.mixer.init()
pygame.mixer.music.load('D:\\estudos\\python\\exercicios python\\Zé do Pastel - O Rei do Campo.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    c = str(input('Deseja parar essa música ? [S/N]')).upper().strip()
    if c[0] == 'S':
        break
    else:
        continue
