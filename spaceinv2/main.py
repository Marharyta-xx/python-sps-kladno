import pygame
import settings
from Player import Player
from Enemy import Enemy

pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders OOP V2")
clock = pygame.time.Clock()

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

enem =1
enemy = Enemy(0,50)
enemy_group = pygame.sprite.Group()
enemy_group.add(enemy)

ENEMY_SPAWN = pygame.USEREVENT +1
pygame.time.set_timer(ENEMY_SPAWN,1500)





running = True
while running:
    clock.tick(settings.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == ENEMY_SPAWN:
            if enem < 5:
                enemy_group.add(Enemy(0,50))
                enem += 1



        
            

    screen.fill(settings.BG_COLOR)
    player_group.update()
    player_group.draw(screen)
    
    enemy_group.update()
    enemy_group.draw(screen)


    pygame.display.flip()
pygame.quit()