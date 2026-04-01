
import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 900
FPS= 60
#Player
PLAYER_WIDTH = 50   
PLAYER_HEIGHT = 30
PLAYER_SPEED = 1
PLAYER_IMAGE_PATH = "img/spaceship.png"
PLAYER_SCALE = 0.08

ENEMY_WIDTH = 40
ENEMY_HEIGHT = 30   
ENEMY_SPEED = 2
ENEMY_IMAGE_PATH = "img/allien1.png"
ENEMY_SCALE = 0.08

BULLET_WIDTH = 5
BULLET_HEIGHT = 10      
BULLET_SPEED = 7
BULLET_IMAGE_PATH = "img/alien_bullet.png"
BULLET_SCALE = 0.02

#Menu 
menu_font = pygame.font.SysFont("Arial", 50)
title_text = menu_font.render("SPACE INVADERS", True, (255, 255, 255),(255,0,0))
play_text = menu_font.render("PLAY", True, (255, 255, 255),(255,0,0))
settings_text = menu_font.render("SETTINGS", True, (255, 255, 255),(255,0,0))
quit_text = menu_font.render("QUIT", True, (255, 255, 255),(255,0,0))
#settings Menu 
res800_text = menu_font.render("800x600", True, (255, 255, 255),(255,0,0))
res1024_text = menu_font.render("1024x768", True, (255, 255, 255),(255,0,0))
res1280_text = menu_font.render("1280x960", True, (255, 255, 255),(255,0,0))
back_text = menu_font.render("BACK", True, (255, 255, 255),(255,0,0))


def update_rect():
    global title_rect, play_rect, settings_rect, quit_rect
    global res800_rect, res1024_rect, res1280_rect, back_rect
    res800_rect = res800_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//3))
    res1024_rect = res1024_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
    res1280_rect = res1280_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT*2//3))
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//12))
    play_rect = play_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//3))
    settings_rect = settings_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
    quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT*2//3))
    back_rect = back_text.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT*5//6))

update_rect()