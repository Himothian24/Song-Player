# Import the modules
import pygame
import button
import os

# Initialize Pygame and the mixer module
pygame.init()
pygame.mixer.init()

# List all songs in the "music" directory
songs = os.listdir("music/")


def get_full_filepaths(directory):
    filepaths = []
    for file in os.listdir(directory):
        path = directory+"/"+file
        if os.path.isdir(path):
            filepaths.extend(get_full_filepaths(path))
        else:
            filepaths.append(path)

    return filepaths


# Set up the display window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Test game")

# Set up the font and render the title text
font = pygame.font.Font(None, 74)
text = font.render('Song Player', True, (255, 255, 255))
text_rect = text.get_rect()
text_rect.center = (screen.get_width() // 2, 50)

print(get_full_filepaths("music"))

  

# Create a list of buttons for each song
# Create buttons for each song
music = get_full_filepaths("music")
button_list = []

y = 100
x = 50

for song in music:
    button_list.append(button.Button(x, y, 200, 50, song))
    x+= 250
    if x > 600:
        y += 100
        x = 50

def main():
    # Main game loop
    while True:
        screen.fill((255, 0, 0))  # Fill the screen with red color
        for event in pygame.event.get():  # Event handling
            if event.type == pygame.QUIT:  # Quit event
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # Mouse click event
                for button in button_list:
                    button.is_clicked()# Check if any button is clicked
                    
        
        for button in button_list:
            button.draw(screen)  # Draw all buttons

        screen.blit(text, text_rect)  # Draw the title text
        
        pygame.display.update()  # Update the display

main()