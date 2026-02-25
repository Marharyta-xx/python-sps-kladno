import pygame
from Player import *
from settings import *
from Block import *
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("uhybaní")
running = True
clock = pygame.time.Clock()

hrac = Player(WIDTH // 2 ,HEIGHT)
hrac_group = pygame.sprite.Group()
hrac_group.add(hrac)

block = Block(WIDTH // 2 ,HEIGHT)
b_group = pygame.sprite.Group()
b_group.add(block)

while running:
    screen.fill((25,25,112))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    hrac_group.update()
    hrac_group.draw(screen)
    b_group.update()
    b_group.draw(screen)
    clock.tick(FPS)
    pygame.display.update()
pygame.quit()