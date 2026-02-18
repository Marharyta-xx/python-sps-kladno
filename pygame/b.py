# import pygame module
import pygame
import time
# import sys library
import sys

# initializing pygame
pygame.init()

clock = pygame.time.Clock()

# Set the window screen size
display_screen = pygame.display.set_mode((500, 500))

# add font style and size
base_font = pygame.font.Font(None, 40)

bomb_timer_text = "bomba vybuchne za {}"
