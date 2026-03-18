import pygame
from Player import *
from settings import *
from Block import *
from random import *

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("uhybaní")
running = True
clock = pygame.time.Clock()

hrac = Player(WIDTH // 2 ,HEIGHT)
hrac_group = pygame.sprite.Group()
hrac_group.add(hrac)

block = Block()
b_group = pygame.sprite.Group()
b_group.add(block)

b_spawn = pygame.USEREVENT + 1
pygame.time.set_timer(b_spawn,1500)

score = 0
score_font = pygame.font.SysFont("Arial", 24)
score_text = score_font.render(f"Score:{score}", True, (255, 255, 255))
score_rect = score_text.get_rect(topleft=(10,10))

while running:
    screen.fill((25,25,112))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == b_spawn:
            b_group.add(Block())
            score += 1
            score_text = score_font.render(f"Score:{score}", True,(255, 255, 255))
            screen.blit(score_text, score_rect)
    
    hrac_group.update()
    hrac_group.draw(screen)
    b_group.update()
    b_group.draw(screen)
    
    if pygame.sprite.spritecollide(hrac, b_group, True, pygame.sprite.collide_mask): #колизия работает при столеновении
        pygame.time.delay(500)
        print("KOLIZE!!!!!!!!!!!!!")
        with open("hightscore.txt", "w") as soubor:
            soubor.write(f"{score}\n")
        running= False



    screen.blit(score_text, score_rect)

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()