import random

import pygame
import settings
from Player import Player
from Enemy import Enemy
from Bullet import Bullet
from Explosion import Explosion
from Boss import Boss
from draw_hp_bar_enemies import draw_hp_bar_enemies

pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders OOP V2")
clock = pygame.time.Clock()

player = Player()
player_group = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
player_group.add(player)
timer = 0
SPAWN_BULLET= pygame.USEREVENT+1
pygame.time.set_timer(SPAWN_BULLET,2000)

enemy = Enemy(0,50)
enemy_group = pygame.sprite.Group()

explosion = Explosion(0,0)
explosion_group = pygame.sprite.Group()



keys = pygame.key.get_pressed()


level = 1 #start level 1
def create_lvl(level): #generovani nepratel pro 1 lvl
    if level > 5:
        enemy = Boss(150, 25)
        enemy_group.add(enemy)
    else:
        x = 75
        y = 25
        for i in range(level):
            for j in range(level*2):
                enemy = Enemy(x,y)
                x += 50
                enemy_group.add(enemy)
            y += 50
            x = 75
create_lvl(level)


running = True
while running:
    clock.tick(settings.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =  False

        if event.type == pygame.KEYDOWN:
            if pygame.K_SPACE and player.cooldown == 0:
                bullet= Bullet(player.rect.left + 5, player.rect.top +40, "Player")
                player_bullet_group.add(bullet)
                bullet= Bullet(player.rect.right - 5, player.rect.top +40, "Player")
                player_bullet_group.add(bullet)
                player.cooldown = pygame.time.get_ticks()

        if event.type == SPAWN_BULLET:
            for enemy in enemy_group:
                if random.randint(1, 100) <= 20:
                    bullet = Bullet(enemy.rect.centerx,enemy.rect.bottom)
                    enemy_bullet_group.add(bullet)

    #kontrola kolizí mezi kulkami a hračem       
    if pygame.sprite.groupcollide(player_group, enemy_group, True, True,pygame.sprite.collide_mask):
        print("sražka")
        running = False
    if pygame.sprite.groupcollide(player_group, enemy_bullet_group, True, True,pygame.sprite.collide_mask):
        print("sražka S PLAYEREM")
        running = False
    #kontrola kolize mezi strělou hráče a nepřítelem
    colided_enemies = pygame.sprite.groupcollide(enemy_group, player_bullet_group, False, True,pygame.sprite.collide_mask)
    for enemy in colided_enemies:
        explosion = Explosion(enemy.rect.centerx, enemy.rect.centery)
        explosion_group.add(explosion)
        enemy.kill()
        print("sražka S ENEMY")


           
    if len(enemy_group) == 0:
        level += 1
        create_lvl(level)
    if level > 5:
        for enemy in enemy_group:
            draw_hp_bar_enemies(screen, enemy.hp, enemy.rect.x, enemy.rect.top-10) 
   

    screen.fill(settings.BG_COLOR)
    player_group.update()
    player_group.draw(screen)
    player_bullet_group.update()
    player_bullet_group.draw(screen)
    enemy_bullet_group.update()
    enemy_bullet_group.draw(screen)
    enemy_group.update()
    enemy_group.draw(screen)
    explosion_group.update()
    explosion_group.draw(screen)
    pygame.display.flip()
pygame.quit()