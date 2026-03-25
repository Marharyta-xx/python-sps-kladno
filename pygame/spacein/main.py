import pygame
from settings import *
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders")
running = True

def vypis_menu():
    screen.blit(title_text, title_rect)
    screen.blit(play_text, play_rect)
    screen.blit(settings_text, settings_rect)
    screen.blit(quit_text, quit_rect)
    
state = "MENU"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
        if state == "MENU":
            if play_rect.collidepoint(mouse_pos):
               state = "PLAYING"
            elif settings_rect.collidepoint(mouse_pos):
                state ="SETTINGS"
            elif quit_rect.collidepoint(mouse_pos):
               running = False
    if state == "MENU":
        screen.fill((0, 0, 0))
        vypis_menu()
