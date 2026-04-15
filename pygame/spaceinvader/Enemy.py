import pygame
import settings
import random as rand
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(settings.ENEMY_IMAGE_PATH.format(rand.randint(1, 5))).convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.image = pygame.transform.scale(self.image,(self.width*settings.ENEMY_SCALE,self.height*settings.ENEMY_SCALE))
        self.rect = self.image.get_rect(top = 0, centerx = rand.randint(0, settings.SCREEN_WIDTH))
        self.counter = 0
        self.direction = "LEFT"  # "RIGHT" pro doprava, "LEFT" pro doleva

    def update(self):
        if self.counter % 90 == 0:
            self.rect.y += settings.ENEMY_SPEED
            if self.direction == "RIGHT":
                self.direction = "LEFT"
            else:
                self.direction = "RIGHT"
        else:
            if self.direction == "RIGHT":
                self.rect.x += settings.ENEMY_SPEED
            else:
                if self.direction == "RIGHT":
                    self.rect.x += settings.ENEMY_SPEED
                else:
                    self.rect.x -= settings.ENEMY_SPEED
        self.counter += 1
        if self.rect.left < 0:
            self.rect.left = 0
            self.direction = "RIGHT"
        if self.rect.right > settings.SCREEN_WIDTH:
            self.rect.right = settings.SCREEN_WIDTH
            self.direction = "LEFT"
            
   