import pygame
import random
import os

pygame.init()
pygame.mixer.init()

song1 = pygame.mixer.Sound("music\Magistar.mp3")

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Test game")

while True:
    screen.fill((255,0,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                song1.play()    
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    pygame.display.update()