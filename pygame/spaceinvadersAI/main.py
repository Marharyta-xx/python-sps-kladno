import pygame
from settings import *
from player import Player
from bullet import Bullet
from enemy import Enemy

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()
running = True

state = "MENU"

player = Player()
bullets = []
enemies = []

spawn_timer = 0

def draw_menu():
    screen.blit(title_text, title_rect)
    screen.blit(play_text, play_rect)
    screen.blit(settings_text, settings_rect)
    screen.blit(quit_text, quit_rect)

while running:
    clock.tick(60)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
  
            if state == "MENU":
                if play_rect.collidepoint(mouse_pos):
                    state = "PLAYING"
                elif settings_rect.collidepoint(mouse_pos):
                    state = "SETTINGS"
                elif quit_rect.collidepoint(mouse_pos):
                    running = False

        if event.type == pygame.KEYDOWN:
            if state == "PLAYING":
                if event.key == pygame.K_SPACE:
                    bullets.append(Bullet(player.rect.centerx, player.rect.top))

    # --- СОСТОЯНИЯ ---
    if state == "MENU":
        draw_menu()

    elif state == "PLAYING":

        # движение игрока
        player.move()

        # спавн врагов
        spawn_timer += 1
        if spawn_timer > 40:
            enemies.append(Enemy())
            spawn_timer = 0

        # обновление пуль
        for bullet in bullets[:]:
            bullet.update()
            if bullet.rect.y < 0:
                bullets.remove(bullet)

        # обновление врагов
        for enemy in enemies[:]:
            enemy.update()
            if enemy.rect.y > 600:
                enemies.remove(enemy)

        # коллизии
        for enemy in enemies[:]:
            for bullet in bullets[:]:
                if enemy.rect.colliderect(bullet.rect):
                    enemies.remove(enemy)
                    bullets.remove(bullet)
                    break

        # отрисовка
        player.draw(screen)

        for bullet in bullets:
            bullet.draw(screen)

        for enemy in enemies:
            enemy.draw(screen)

        # выход в меню
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            state = "MENU"

    elif state == "SETTINGS":
        text = menu_font.render("SETTINGS", True, (255, 255, 255))
        screen.blit(text, (250, 250))

    pygame.display.update()

pygame.quit()