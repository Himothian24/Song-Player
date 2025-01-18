import pygame
import sys

pygame.init()
pygame.mixer.init()

song1 = pygame.mixer.Sound("music/Raving Energy (faster).mp3")
song_2 = pygame.mixer.Sound("music/Deep and Dirty.mp3")
screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Test game")

font = pygame.font.Font(None, 74)
text = font.render('Song Player', True, (255, 255, 255))
text_rect = text.get_rect()
text_rect.center = (screen.get_width() // 2, 50)

class Button():
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.text_surf = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)
        screen.blit(self.text_surf, self.text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
            return False

song = Button(300, 400, 200, 50, "Song 2")
song2 = Button(50, 400, 200, 50, "Song")

while True:
    screen.fill((255,0,0))
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if song.is_clicked(event):
            pygame.mixer.pause()
            song1.play()
        if song2.is_clicked(event):
            pygame.mixer.pause()
            song_2.play()

    screen.blit(text, text_rect)
    song2.draw(screen)
    song.draw(screen)

    
    
    pygame.display.update()