# Import the modules
import pygame
import os

# Initialize Pygame and the mixer module
pygame.init()
pygame.mixer.init()

# List all songs in the "music" directory
songs = os.listdir("music/")

# Function to extract the song name from the file path
def get_song_name(song):
    song = song.split("/")[-1]  # Get the file name
    song = song.split(".")[0]   # Remove the file extension
    return song
        
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

# Button class to create and manage buttons
class Button():
    def __init__(self, x, y, width, height, song):
        self.rect = pygame.Rect(x, y, width, height)  # Button rectangle
        self.song = pygame.mixer.Sound(song)  # Load the specific song for this button
        self.text = get_song_name(song)  # Button text
        size = 25 - (len(self.text) // 10)  # Adjust font size based on text length
        self.font = pygame.font.Font(None, size)
        self.text_surf = self.font.render(self.text, True, (255, 255, 255))  # Render text
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)  # Center text in button

        

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)  # Draw button rectangle
        screen.blit(self.text_surf, self.text_rect)  # Draw button text

    def is_clicked(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):  # Check if button is clicked
            pygame.mixer.pause()  # Pause any currently playing song
            self.song.play()  # Play the button's song
        return False


print(get_full_filepaths("music"))


# Create a list of buttons for each song
# Create buttons for each song
music = get_full_filepaths("music")
button_list = []

y = 100
x = 50

for song in music:
    button_list.append(Button(x, y, 200, 50, song))
    x+= 250
    if x > 600:
        y += 100
        x = 50
    

# Main game loop
while True:
    screen.fill((255, 0, 0))  # Fill the screen with red color
    for event in pygame.event.get():  # Event handling
        if event.type == pygame.QUIT:  # Quit event
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:  # Mouse click event
            for button in button_list:
                button.is_clicked()  # Check if any button is clicked
    
    for button in button_list:
        button.draw(screen)  # Draw all buttons

    screen.blit(text, text_rect)  # Draw the title text
    
    pygame.display.update()  # Update the display

