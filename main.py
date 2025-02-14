import pygame
import os

pygame.init()
pygame.mixer.init()

songs = os.listdir("music/")



def get_song_name(song):
    song = song.split("/")[-1]
    song = song.split(".")[0]

    return song
    
screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Test game")

font = pygame.font.Font(None, 74)
text = font.render('Song Player', True, (255, 255, 255))
text_rect = text.get_rect()
text_rect.center = (screen.get_width() // 2, 50)

class Button():
    def __init__(self, x, y, width, height, song):
       
        self.rect = pygame.Rect(x, y, width, height)
        self.text = get_song_name(song)
        size = 25-(len(self.text)//10)
        self.font = pygame.font.Font(None, size)
        self.text_surf = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)
        self.song = pygame.mixer.Sound("music/"+song)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)
        screen.blit(self.text_surf, self.text_rect)

    def is_clicked(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.mixer.pause()
            self.song.play()
        return False

button_list = []
x = 50
for song in songs:
    button_list += [Button(x, 400, 200, 50, song)]
    x = x + 250


while True:
    screen.fill((255,0,0))
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for thing in button_list:
                thing.is_clicked()
    
    for thing in button_list:
        thing.draw(screen)

    screen.blit(text, text_rect)
    
    pygame.display.update()