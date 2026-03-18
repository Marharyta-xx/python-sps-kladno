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

B_SPAWN = pygame.USEREVENT + 1
pygame.time.set_timer(b_spawn,1500)

score = 0
score_font = pygame.font.SysFont("Arial", 24)
score_text = score_font.render(f"Score:{score}", True, (255, 255, 255))
score_rect = score_text.get_rect(topleft=(10,10))


#try:
   # with open("hightscore.txt", "w") as soubor:
        #hightscore = int(soubor.read().strip())



while running:
    screen.fill((25,25,112))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == B_SPAWN:
            b_group.add(Block())
            score += 1
            score_text = score_font.render(f"Score:{score}", True,(255, 255, 255))
        if score % 2 == 0 and score != 0:
            spawning_timer = max(500, spawning_timer - 100)
            pygame.time.set_timer(B_SPAWN, spawning_timer)
        


            screen.blit(score_text, score_rect)

    
    hrac_group.update()
    hrac_group.draw(screen)
    b_group.update()
    b_group.draw(screen)
    
    if pygame.sprite.spritecollide(hrac, b_group, True, pygame.sprite.collide_mask): #колизия работает при столеновении
        pygame.time.delay(500)
        print("KOLIZE!!!!!!!!!!!!!")
        if score >= hightscore:
            hightscore = score
        with open("hightscore.txt", "w") as soubor:
            soubor.write(f"{hightscore}\n")
        #with open("hightscore.txt", "r") as soubor:



        running = False



    screen.blit(score_text, score_rect)

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()